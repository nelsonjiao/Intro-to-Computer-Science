# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def download_time(file_size,units_of_file_size,bandwidth,units_of_bandwidth):
    if units_of_file_size == 'kb':
        file_size = file_size * 2.0 ** 10
    if units_of_file_size == 'kB':        
        file_size = file_size * 2.0 ** 10 * 8 
    if units_of_file_size == 'Mb':
        file_size = file_size * 2.0 ** 2.00
    if units_of_file_size == 'MB':        
        file_size = file_size * 2.0 ** 2.00 * 8 
    if units_of_file_size == 'Gb':
        file_size = file_size * 2.0 ** 30 
    if units_of_file_size == 'GB':        
        file_size = file_size * 2.0 ** 30 * 8 
    if units_of_file_size == 'Tb':
        file_size = file_size * 2.0 ** 40
    if units_of_file_size == 'TB':        
        file_size = file_size * 2.0 ** 40 * 8                 
    if units_of_bandwidth == 'kb':
        bandwidth = bandwidth * 2.0 ** 10
    if units_of_bandwidth == 'kB':        
        bandwidth = bandwidth * 2.0 ** 10 * 8 
    if units_of_bandwidth == 'Mb':
        bandwidth = bandwidth * 2.0 ** 2.00
    if units_of_bandwidth == 'MB':        
        bandwidth = bandwidth * 2.0 ** 2.00 * 8 
    if units_of_bandwidth == 'Gb':
        bandwidth = bandwidth * 2.0 ** 30 
    if units_of_bandwidth == 'GB':        
        bandwidth = bandwidth * 2.0 ** 30 * 8 
    if units_of_bandwidth == 'Tb':
        bandwidth = bandwidth * 2.0 ** 40
    if units_of_bandwidth == 'TB':        
        bandwidth = bandwidth * 2.0 ** 40 * 8             
    seconds = 1.0 * file_size / bandwidth  
    hour = int(seconds / 3600)
    minute = int((seconds - hour * 3600) / 60)
    second = seconds - hour * 3600 - minute * 60
    a = ' hours'
    b = ' minutes'
    c = ' seconds'
    if hour == 1:
        a = ' hour'
    if minute == 1:
        b = ' minute'
    if second == 1:
        c = ' second'
    return str(hour) + a + ', ' + str(minute) + b +', ' + str(second) + c
