import os


def look_for_errors(text: str, filename: str):
	for i, line in enumerate(text.split('\n')):
		if line.startswith('#'):
			continue
		if line.startswith("var"):
			if not ":" in line:
				print(f"[{filename}] Line {i + 1}: variable might not be statically typed: {line}")


def scan_directory(directory):
	for root, dirs, files in os.walk(directory):
		for file in files:
			if file.endswith(".gd"):
				with open(os.path.join(root, file), 'r', encoding="UTF-8") as f:
					look_for_errors(f.read(), file)
			if not file.islower():
				print(f"Filename is not lowercase: {file}")


scan_directory("./")
