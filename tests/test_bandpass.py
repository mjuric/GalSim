# Copyright 2012-2014 The GalSim developers:
# https://github.com/GalSim-developers
#
# This file is part of GalSim: The modular galaxy image simulation toolkit.
#
# GalSim is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GalSim is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GalSim.  If not, see <http://www.gnu.org/licenses/>
#
import os
import numpy as np
import galsim

path, filename = os.path.split(__file__)
datapath = os.path.abspath(os.path.join(path, "../examples/data/"))

def test_Bandpass_mul():
    """Check that Bandpasses multiply like I think they should...
    """
    a = galsim.Bandpass(galsim.LookupTable([1,2,3,4,5], [1,2,3,4,5]))
    b = galsim.Bandpass(galsim.LookupTable([1.1,2.2,3.0,4.4,5.5], [1.11,2.22,3.33,4.44,5.55]))
    # Bandpass * Bandpass
    c = a*b
    np.testing.assert_almost_equal(c.blue_limit, 1.1, 10,
                                   err_msg="Found wrong blue limit in Bandpass.__mul__")
    np.testing.assert_almost_equal(c.red_limit, 5.0, 10,
                                   err_msg="Found wrong red limit in Bandpass.__mul__")
    np.testing.assert_almost_equal(c(3.0), 3.0 * 3.33, 10,
                                   err_msg="Found wrong value in Bandpass.__mul__")
    np.testing.assert_almost_equal(c(1.1), a(1.1)*1.11, 10,
                                   err_msg="Found wrong value in Bandpass.__mul__")
    np.testing.assert_almost_equal(c(5.0), b(5.0)*5, 10,
                                   err_msg="Found wrong value in Bandpass.__mul__")
    np.testing.assert_array_almost_equal(c.wave_list, [1.1, 2, 2.2, 3, 4, 4.4, 5],
                                         err_msg="wrong wave_list in Bandpass.__mul__")
    # Bandpass * fn
    d = lambda w: w**2
    e = c*d
    np.testing.assert_almost_equal(e(3.0), 3.0 * 3.33 * 3.0**2, 10,
                                   err_msg="Found wrong value in Bandpass.__mul__")
    np.testing.assert_array_almost_equal(e.wave_list, [1.1, 2, 2.2, 3, 4, 4.4, 5],
                                         err_msg="wrong wave_list in Bandpass.__mul__")
    # fn * Bandpass
    e = d*c
    np.testing.assert_almost_equal(e(3.0), 3.0 * 3.33 * 3.0**2, 10,
                                   err_msg="Found wrong value in Bandpass.__mul__")
    np.testing.assert_array_almost_equal(e.wave_list, [1.1, 2, 2.2, 3, 4, 4.4, 5],
                                         err_msg="wrong wave_list in Bandpass.__mul__")
    # Bandpass * scalar
    f = e * 1.21
    np.testing.assert_almost_equal(f(3.0), 3.0 * 3.33 * 3.0**2 * 1.21, 10,
                                   err_msg="Found wrong value in Bandpass.__mul__")
    np.testing.assert_array_almost_equal(f.wave_list, [1.1, 2, 2.2, 3, 4, 4.4, 5],
                                         err_msg="wrong wave_list in Bandpass.__mul__")
    # scalar * Bandpass
    f = 1.21 * e
    np.testing.assert_almost_equal(f(3.0), 3.0 * 3.33 * 3.0**2 * 1.21, 10,
                                   err_msg="Found wrong value in Bandpass.__mul__")
    np.testing.assert_array_almost_equal(f.wave_list, [1.1, 2, 2.2, 3, 4, 4.4, 5],
                                         err_msg="wrong wave_list in Bandpass.__mul__")

def test_Bandpass_div():
    """Check that Bandpasses multiply like I think they should...
    """
    a = galsim.Bandpass(galsim.LookupTable([1,2,3,4,5], [1,2,3,4,5]))
    b = galsim.Bandpass(galsim.LookupTable([1.1,2.2,3.0,4.4,5.5], [1.11,2.22,3.33,4.44,5.55]))
    # Bandpass / Bandpass
    c = a/b
    np.testing.assert_almost_equal(c.blue_limit, 1.1, 10,
                                   err_msg="Found wrong blue limit in Bandpass.__mul__")
    np.testing.assert_almost_equal(c.red_limit, 5.0, 10,
                                   err_msg="Found wrong red limit in Bandpass.__mul__")
    np.testing.assert_almost_equal(c(3.0), 3.0 / 3.33, 10,
                                   err_msg="Found wrong value in Bandpass.__mul__")
    np.testing.assert_almost_equal(c(1.1), a(1.1)/1.11, 10,
                                   err_msg="Found wrong value in Bandpass.__mul__")
    np.testing.assert_almost_equal(c(5.0), 5/b(5.0), 10,
                                   err_msg="Found wrong value in Bandpass.__mul__")
    np.testing.assert_array_almost_equal(c.wave_list, [1.1, 2, 2.2, 3, 4, 4.4, 5],
                                         err_msg="wrong wave_list in Bandpass.__mul__")
    # Bandpass / fn
    d = lambda w: w**2
    e = c/d
    np.testing.assert_almost_equal(e(3.0), 3.0 / 3.33 / 3.0**2, 10,
                                   err_msg="Found wrong value in Bandpass.__mul__")
    np.testing.assert_array_almost_equal(e.wave_list, [1.1, 2, 2.2, 3, 4, 4.4, 5],
                                         err_msg="wrong wave_list in Bandpass.__mul__")
    # fn / Bandpass
    e = d/c
    np.testing.assert_almost_equal(e(3.0), 3.0**2 / (3.0 / 3.33), 10,
                                   err_msg="Found wrong value in Bandpass.__mul__")
    np.testing.assert_array_almost_equal(e.wave_list, [1.1, 2, 2.2, 3, 4, 4.4, 5],
                                         err_msg="wrong wave_list in Bandpass.__mul__")
    # Bandpass / scalar
    f = e / 1.21
    np.testing.assert_almost_equal(f(3.0), (3.0**2 / (3.0 / 3.33)) / 1.21, 10,
                                   err_msg="Found wrong value in Bandpass.__mul__")
    np.testing.assert_array_almost_equal(f.wave_list, [1.1, 2, 2.2, 3, 4, 4.4, 5],
                                         err_msg="wrong wave_list in Bandpass.__mul__")
    # scalar / Bandpass
    f = 1.21 / e
    np.testing.assert_almost_equal(f(3.0), 1.21 / (3.0**2 / (3.0 / 3.33)), 10,
                                   err_msg="Found wrong value in Bandpass.__mul__")
    np.testing.assert_array_almost_equal(f.wave_list, [1.1, 2, 2.2, 3, 4, 4.4, 5],
                                         err_msg="wrong wave_list in Bandpass.__mul__")

def test_Bandpass_wave_type():
    """Check that `wave_type='ang'` works in Bandpass.__init__
    """
    a0 = galsim.Bandpass(os.path.join(datapath, 'LSST_r.dat'))
    a1 = galsim.Bandpass(os.path.join(datapath, 'LSST_r.dat'), wave_type='ang')

    np.testing.assert_approx_equal(a0.red_limit, a1.red_limit*10,
                                   err_msg="Bandpass.red_limit doesn't respect wave_type")
    np.testing.assert_approx_equal(a0.blue_limit, a1.blue_limit*10,
                                   err_msg="Bandpass.blue_limit doesn't respect wave_type")
    np.testing.assert_approx_equal(a0.effective_wavelength, a1.effective_wavelength*10,
                                   err_msg="Bandpass.effective_wavelength doesn't respect wave_type")

    b0 = galsim.Bandpass(galsim.LookupTable([1,2,3,4,5], [1,2,3,4,5]))
    b1 = galsim.Bandpass(galsim.LookupTable([10,20,30,40,50], [1,2,3,4,5]), wave_type='ang')
    np.testing.assert_approx_equal(b0.red_limit, b1.red_limit,
                                   err_msg="Bandpass.red_limit doesn't respect wave_type")
    np.testing.assert_approx_equal(b0.blue_limit, b1.blue_limit,
                                   err_msg="Bandpass.blue_limit doesn't respect wave_type")
    np.testing.assert_approx_equal(b0.effective_wavelength, b1.effective_wavelength,
                                   err_msg="Bandpass.effective_wavelength doesn't respect wave_type")
    np.testing.assert_allclose(b0([1,2,3,4,5]), b1([1,2,3,4,5]),
                               err_msg="Bandpass.__call__ doesn't respect wave_type")

if __name__ == "__main__":
    test_Bandpass_mul()
    test_Bandpass_div()
    test_Bandpass_wave_type()