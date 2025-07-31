 
#todo Implement Multi-rank and Dynamic spritesheet class
# - Multirank means it can index into block-like spritesheets that have more than one row of sprites
# - Dynamic means it does not Cache the frames ahead of time, but instead it stores indicies for them and Dynamically generates those frames as needed.

#? The opposite of Multi-rank Dynamic spritesheet (mr-d) would be our Single-rank Frame-Caching spritesheet (sr-fc)