
import math
import os
import ctypes

PATH_MAX = 4096
UTIME_OMIT = (1 << 30) - 2
UTIME_NOW = (1 << 30) - 1
FILE_NAME = 'hello'
DATE1 = 1900000000 # Sun Mar 17 11:46:40 MDT 2030
DATE2 = 1950000000 # Fri Oct 17 04:40:00 MDT 2031

class timespec(ctypes.Structure):
	_fields_ = [
		('tv_sec', ctypes.c_long),
		('tv_nsec', ctypes.c_long)
		]

libc = ctypes.CDLL(None)

utimensat = libc.utimensat
utimensat.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_char), timespec * 2, ctypes.c_int)
utimensat.restype = ctypes.c_int

def get_path_buffer(in_path):
	return ctypes.create_string_buffer(in_path.encode(), size = PATH_MAX)

def run_test(in_path):
	
	def set_times(a_sec, a_nsec, m_sec, m_nsec):
		in_time = (timespec * 2)()
		in_time[0].tv_sec = a_sec
		in_time[0].tv_nsec = a_nsec
		in_time[1].tv_sec = m_sec
		in_time[1].tv_nsec = m_nsec
		utimensat(0, file_path_buffer, in_time, 0)
		
	def get_times():
		stat_dict = os.stat(file_path)
		a_sec = int(math.floor(stat_dict.st_atime_ns / 10 ** 9))
		a_nsec = int(stat_dict.st_atime_ns - a_sec * 10 ** 9)
		m_sec = int(math.floor(stat_dict.st_mtime_ns / 10 ** 9))
		m_nsec = int(stat_dict.st_mtime_ns - m_sec * 10 ** 9)
		return a_sec, a_nsec, m_sec, m_nsec
	
	file_path = os.path.abspath(os.path.join(in_path, FILE_NAME))
	file_path_buffer = get_path_buffer(file_path)
	
	if not os.path.isfile(file_path):
		with open(file_path, 'w+') as f:
			f.write('')
	
	set_times(0, UTIME_NOW, 0, UTIME_NOW)
	print(get_times())
	set_times(DATE1, 0, DATE2, 0)
	print(get_times())
	set_times(0, UTIME_NOW, 0, UTIME_OMIT)
	print(get_times())
	set_times(DATE1, 0, DATE2, 0)
	print(get_times())
	set_times(0, UTIME_OMIT, 0, UTIME_NOW)
	print(get_times())
	set_times(0, UTIME_NOW, 0, UTIME_NOW)
	print(get_times())
	set_times(0, UTIME_OMIT, DATE2, 0)
	print(get_times())
	set_times(0, UTIME_NOW, 0, UTIME_NOW)
	print(get_times())
	set_times(DATE1, 0, 0, UTIME_OMIT)
	print(get_times())

if __name__ == '__main__':
	run_test(os.path.join(os.getcwd(), 'mnt0'))
	#run_test(os.path.join(os.getcwd(), 'mnt2'))
	run_test(os.path.join(os.getcwd(), 'mnt3h'))
