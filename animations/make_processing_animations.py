import os
import re
import illustrator

def main():
	
	ngons=[i for i in os.listdir('outputs') if re.match("[0-9]+",i)]
	
	for ngon in ngons:
		
		animations=[i for i in os.listdir(os.path.join('outputs',ngon)) if i.endswith('.json')]
		for animation in animations:
			illustrator.make_processing_animation(animation)


if __name__=="__main__":
	main()