# -*- coding: utf-8 -*-

"""
preprocess
~~~~~~~~~~

this module contains all the common processing of OCT rawdata before reconstruct it
into images

"""

import numpy as np
from scipy.interpolate import interp1d
from . import decors

def adjust_phase():
    pass

def resample(x, y, xq, method='cubic'):
    """
    resample y at xq, if y is higher than 1 dimension, the resampling is done in last dimension

    :param y: the data/spectrum as numpy array to be resampled
    :param x: the x coordinates of data in axis
    :param xq: the queried points' x coordinates, in range of [0, 1]
    :return: resampled y at xq
    """
    if y.ndim == 1:
        interp = interp1d
    elif y.ndim == 2:
        interp = decors.proc_along_axis(interp1d)
    elif y.ndim == 3:
        interp = decors.proc_along_axis(interp1d)

    interp = interp1d(x, y, kind=method, bounds_error=False, fill_value=0)
    y_resampled = interp(xq)

    linear_x = np.linspace(0, 1, data.shape[-1]).astype(np.float32)
    cali_x = np.polyval(calib_coeff, linear_x)
    cali_x[cali_x<0] = 0
    cali_x[cali_x>1] = 1
    #interp for 1D or 2D data.
    data = data.reshape(-1,data.shape[-1])
    calied_data = np.zeros_like(data)
    calied_data = np.interp1d(linear_x, data, kind=method)(cali_x)
    return calied_data

def recon_img():
    img = np.fft

    pass

def recon_doppler():
    pass

def filter(data, axis=0, win=[]):

    pass


def calc_dc(data, axis=0, method='mean'):
    if method == 'mean':
        dc = data.mean(0)
    elif method == 'median':
        dc = np.median(data[10::10, :], 0)
    return dc


def gen_calib(data, win = [], order = 4, conf_file_path = []):
    '''
    function gen_calib_coeff(data, win = [], file_path = [])
    generate the calibration coeff data as non-linear array from 0 to 1
    data: input data
    win: window to filter the data for calcuation
    file_path: file to save the calib_coeff
    '''
    data = data if (len(data.shape) == 1) else data.mean(0)
    #plt.plot(data)
    if len(win):
        data = fft_filt_pass(data, win)
    calib_data = np.unwrap(np.angle(hilbert(data)));
    calib_data = (calib_data - calib_data[0]) /(calib_data[-1]-calib_data[0])
    linear_x = np.linspace(0,1,calib_data.size)
    calib_coeff =  np.polyfit(linear_x[50:-50], calib_data[50:-50], order)
    if len(conf_file_path):
        write_cfg_file(conf_file_path, 'SYS', 'Calibration', calib_coeff) #update the number in the oct.ini file
    return calib_coeff

def calibrate_data(data, calib_coeff, interp_method = 'linear'):
    '''
    function calibrate_data(data, calib_coeff)
    calibrate the non-linear K data
    data: input data
    calib_coeff: the calibration coeff from function gen_calib_coeff
    '''
    linear_x = np.linspace(0,1,data.shape[-1]).astype(np.float32)
    calib_data = np.polyval(calib_coeff, linear_x)
    calib_data[calib_data<0] = 0
    calib_data[calib_data>1] = 1
    #interp for 1D or 2D data.
    data = data.reshape(-1,data.shape[-1])
    calied_data = np.zeros_like(data)
    calied_data = interp1d(linear_x, data, kind=interp_method)(calib_data)
    return calied_data


def gen_disp(data, win = [], conf_file_path = []):
    '''
    function gen_disp_coeff(data, win = [], file_path = [])
    generate the disp coeff (3rd and 2nd order) by mirror signal
    data: input data
    win: the window to filter data
    update_cfg: update pyoct.ini
    '''
    data = data if (len(data.shape) == 1) else data.mean(0)
    #plt.plot(data)
    if len(win):
        data = fft_filt_pass(data, win)
    phase = np.unwrap(np.angle(hilbert(data)));
    linear_x = np.linspace(0,1,phase.size)
    disp_coeff = np.polyfit(linear_x[50:-50], phase[50:-50], 3)[0:2]
#    disp_data = np.polyval(np.append(disp_coeff, [-disp_coeff.sum, 0]), linear_x)
    if len(conf_file_path):
        write_cfg_file(conf_file_path, 'SYS', 'Dispersion', disp_coeff) #update the number in the oct.ini file
#    if len(data_file_path):
#        save_binary_data(disp_data, data_file_path)
    return disp_coeff


def gen_disp2(data, win = [0, 1], conf_file_path = []):
    '''
    function gen_disp_coeff2(data, win = [], file_path = [])
    generate the disp coeff (3rd and 2nd order) iteratively
    data: input data
    win: the window to filter data
    update_cfg: update pyoct.ini
    '''
    def img_entropy(disp_coeff, data, win):
        nondisp_data = corr_dispersion(data, disp_coeff)
        Image = abs(fftpack.fft(nondisp_data))
        Image = Image[:,win[0]:win[1]]
        Image /= Image.sum()
        return -(Image*np.log(Image)).sum()
    #select window to minimize the computation
    if all(0<=foo<=1 for foo in win):
        win = [data.shape[-1] * win[0]/2,data.shape[-1] * win[1]/2]
    fmin(img_entropy, disp_coeff, data, win)
    if len(conf_file_path):
        write_cfg_file(conf_file_path, 'SYS', 'Dispersion', disp_coeff) #update the number in the oct.ini file
    return disp_coeff


def corr_dispersion(data, disp_coeff):
    '''
    compensate dispersion using 3rd and 2nd order dispersionc oeff
    '''
    linear_x = np.linspace(0,1,data.shape[-1]).astype(np.float32)
    disp_coeff = np.polyval(np.append(disp_coeff, [-disp_coeff.sum(), 0]), linear_x)
    nondisp_data = data * np.exp(-1j*disp_coeff) #the value of data changes, since data is immutable
    return nondisp_data

def corr_phase_jit(data):
    pass

def gen_fr_data(data, r2i_ratio, bandwidth = 0.4):
    '''
    function gen_fr_data(data, r2i_ratio, bandwidth = 0.4)
    generate the complex data for full range OCT reconstruction
    data: input data
    r2i_ratio: the real to imaginary ratio, tan(phi) where phi is phase modulation depth
    bandwidth: the bandwidth to separate the real and imaginary part.
    '''
    data = data.T
    alt_filter =  np.array([1, -1] * data.shape[-1]/2)
    real_data = fft_filt_pass(data, [0,bandwidth *data.shape[-1]/2])
    imag_data = fft_filt_pass(data * alt_filter, [0,bandwidth *data.shape[-1]/2])
    fr_data= real_data + 1j * imag_data;
    return fr_data


#def pre_proc_oct_data(data, calib_coeff=[], disp_coeff=[], reshape_win=[]):
#    if len(calib_coeff):
#        data = calibrate_data(data, calib_coeff, )
#    if len(reshape_win):
#        data *= eval('np.' + reshape_win + '('+str(data.shape[-1])+')')
#    if len(disp_coeff):
#        data = corr_dispersion(data, disp_coeff)
#    return data


def recon_magnitude_img(data, full_range = 0, fft_num = 2048, scale = 'log'):
    '''
    function recon_magnitude_img(data, real_input = True, depth_dim = 1024, scale = 'log', disp_range = [0.5, 0])
    reconstruct the amplitude image:
    data: input data
    full_range: if ture, use full range
    depth_dim: pixel num in depth
    scale: log or linear
    disp_range: display range for contrast/dynamic range, relative value if within [0,1],
    '''
    img = fftpack.fft(data,fft_num)
#    if np.any(np.imag(data)):
#        img = fftpack.fft(data,fft_num)
#    else:
#        img = fftpack.rfft(data,fft_num)
    if not full_range:
        img = img[:,:fft_num/2]

    if scale =='log':
        img = 20 * np.log10(abs(img))
    elif scale == 'linear':
        img = abs(img)
    return img


def recon_phase_img(data, thresh = 0, full_range =0, fft_num = 2048, filter_size = 3):
    '''
    function recon_magnitude_img(data, real_input = True, depth_dim = 1024, scale = 'log', disp_range = [0.5, 0])
    reconstruct the amplitude image:
    data: input data
    full_range: if ture, use full range
    depth_dim: pixel num in depth
    scale: log or linear
    disp_range: display range for contrast/dynamic range, relative value if within [0,1],
    '''
    img = fftpack.fft(data,fft_num)
#    if np.any(np.imag(data)):
#        img = fftpack.fft(data,fft_num)
#    else:
#        img = fftpack.rfft(data,fft_num)
    if not full_range:
        img = img[:,:fft_num/2]

    img = img[:-1]*np.conjugate(img[1:])
    if filter_size > 1:
        img = ndimage.uniform_filter(img.real, filter_size) + 1j * ndimage.uniform_filter(img.imag,filter_size)
    img = np.angle(np.append(img, [img[-1]], 0))
#    img +=np.pi
#    if all(0<=foo<=1 for foo in disp_range):
#        mag_min = np.percentile(img, disp_range[0]*100.0)
#        mag_max = np.percentile(img, 100.0-disp_range[1]*100.0)
#    else:
#        mag_min, mag_max = disp_range
#    mag_min, mag_max = disp_range
#    img = (img - mag_min) /(mag_max-mag_min)
#    if img_format is'uint8':
#        img = img * (img >= 0) *(img <= 1) + (img>1)
#        img = np.uint8(img*255)

    return  img

def get_display_range(image, disp_range = np.array([50, 100])):
    disp_range = [max(min(disp_range), 0), min(max(disp_range), 100)]
    mag_min = np.percentile(image, disp_range[0])
    mag_max = np.percentile(image, disp_range[1])
    return np.array([mag_min, mag_max])

def rescale_range(image, disp_range, img_format = 'uint8'):
    #re-scale
    image = (image - disp_range[0]) /(disp_range[1]-disp_range[0])
    image[image<0] = 0
    image[image>1] = 1
    if img_format is'uint8':
        image = np.uint8(image*255)
    else:
        image = np.uint16(image*65535)
    return image

def get_psf(data, disp_coeff, calib_coeff):
    data = calibrate_data(data, calib_coeff,'cubic')
    data = corr_dispersion(data, disp_coeff)
    psf = recon_magnitude_img(data, 'log').mean(0)
#    if any(win>1):
#        psf = psf[win[0]:win[1]]
#    else:
#        psf = psf[win[0]*psf.size:win[1]*psf.size]
    return psf

# test code
if __name__ == '__main__':
    import matplotlib.pyplot as plt
#    ref = read_binary_data('T:\\ZYtemp\\SoftwareDev\\PyOCT\\conf\\BT_SDOCT.ref')
    calib_coeff = read_binary_data('T:\\ZYtemp\\SoftwareDev\\PyOCT\\conf\\BT_SDOCT.clb')
    disp_coeff = read_binary_data('T:\\ZYtemp\\SoftwareDev\\PyOCT\\conf\\BT_SDOCT.dsp')
    for i in range(1, 12, 1):
        data = read_binary_data('T:\ZYtemp\\2012-05-30 benchtop sdoct\\signal roll off\\OCTImage' + "%.2d" % i +'.raw', data_dim = 1024, input_format = 'uint16')
        ref = gen_ref(data, 'median')
        data -= ref
#        ref = read_binary_data(ref_source, data_dim, input_format = 'uint16').mean(0)
        calied_data = calibrate_data(data, calib_coeff)
        calied_data = calied_data * np.exp(-1j*disp_coeff) #remove disperison
        mag_img = recon_magnitude_img(calied_data)
        plt.figure(1)
        plt.imshow(mag_img)
        plt.ginput()
