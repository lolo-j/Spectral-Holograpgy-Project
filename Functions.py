
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack 


# In[10]:


def graph_amp_ft(a,start,end): #graphs amplitude graph, fourier transform, power spectrum, and phase
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.signal import find_peaks
    #Amplitude
    time = a[0,:]
    left = a[1,:]
    right = a[2,:]
    ################################
    f = plt.figure(figsize=(15,5))
    ax = f.add_subplot(121)
    ax2 = f.add_subplot(122)
    ax.plot(time, left , label="Left channel")
    ax.plot(time, right, label="Right channel")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    
    #FT
    g=left[start:end]
    t=time[start:end]
    dt = 1/44100 # increment between times in time array
    G = fftpack.fft(g) # FFT of g
    f = fftpack.fftfreq(g.size, d=dt) # frequenies f[i] of g[i]
    f = fftpack.fftshift(f) # shift frequencies from min to max 
    ax2.plot(f, np.real(G), color='black', label='real part')
    ax2.set_xlabel("Frequency (Hz)")
    #ax2.plot(f, np.imag(G), color='blue', label='imaginary part')
    plt.show()
    
    
    r = plt.figure(figsize=(15,5))
    ax = r.add_subplot(121)
    ax2 = r.add_subplot(122)
    
    #Power Spectrum
    power_s=(np.abs(G))**2
    ax.plot(f, power_s)
    ax.set_xlabel("Frequency [Hz]")

    
    #Phase thing
    phase=np.angle(G)
    ax2.plot(f, phase)
    ax2.set_xlabel("Frequency [Hz]")
    ax2.set_ylabel("Angle [rad]")
    plt.show()
    return(power_s,f,G,phase)
    
def find_frequency(ps,ftf): #Pulls out frequency from power spectrum
    from scipy.signal import find_peaks
    i=find_peaks(ps,height=0.1e12)[0]
    y=[ftf[j] for j in i]
    return(y,i)

