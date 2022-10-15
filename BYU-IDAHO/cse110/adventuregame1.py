choices_for_Options=input("Choices are: RUN, LOOK, FASTER")
print()
Options= input('Please choose an option: ')

if Options.capitalize() == 'Run':
    print('You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?')
else: 
    print()

if Options.capitalize() == 'Look':
    print('You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?')
else:
    print()

if Options.capitalize() == 'Faster':
    print('You pick nothing and decide to walk down the Path without any source of illumination. You hear a sound and decide to walk a little faster. You then hear a roar of an animal that sounds just like a large grizzly bear. Do you want to WALK FASTER or HIDE?')
else:
    print()    