from pet import Pet

# Create a pet
buddy = Pet("Buddy")

# Check initial status
buddy.get_status()

# Feed the pet
buddy.eat()
buddy.get_status()

# Let the pet sleep
buddy.sleep()
buddy.get_status()

# Play with the pet
buddy.play()
buddy.get_status()

# Train the pet
buddy.train("roll over")
buddy.train("sit")

# Show learned tricks
buddy.show_tricks()
