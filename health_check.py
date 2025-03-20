import psutil

def check_cpu():
	"""Check CPU usage and warn if it's too high."""
	cpu_usage = psutil.cpu_percent(interval=1)  # Gets CPU usage over 1 second
	if cpu_usage > 80:  # If the CPU usage is above 80%, its a problem
		print(f"Hgih CPU Usage: {cpu_usage}%")
	else:
		print(f"CPU Usage is normal: {cpu_usage}%")
		
def check_memory():
	"""Check memory (RAM) usage and warn if too high."""
	memory = psutil.virtual_memory()  # Gets memory (RAM) details
	if memory.percent > 80:  # If the Ram usage is above 80%, its a problem
		print(f"High Memory Usage: {memory.precent}%")
	else:
		print(f"Memory Usage is normal: {memory.percent}%")
		
def check_disk():
	"""Check disk space and warn if storage is low."""
	disk = psutil.disk_usage('/')  # Gets disk space details from the main drive when '/' is used
	if disk.percent > 80:  # If more than 80% of storage is used, it's a problem
		print(f"Low Disk Space: {disk.percent}% used")
	else:
		print(f"Disk Space is fine: {disk.percent}% used")
		
if __name__ == "__main__":
	"""Run all checks when script is executed."""
	print("System Health Check")
	check_cpu()
	check_memory()
	check_disk()