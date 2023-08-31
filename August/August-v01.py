def reward_function(params):

    # Read input variables
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']

    # Set the speed threshold based your action space
    SPEED_THRESHOLD = 1.0

    if not all_wheels_on_track:
        # Penalize if the car goes off track
        reward = 1e-3
    elif speed < SPEED_THRESHOLD:
        # Penalize if the car goes too slow
        reward = 0.5
    else:
        # High reward if the car stays on track and goes fast
        reward = 1.0
        if speed > SPEED_THRESHOLD*2:
            reward *= 2
        if speed > SPEED_THRESHOLD*3:
            reward *= 3
        if speed > SPEED_THRESHOLD*5:
            reward *= 5
        

    return float(reward)
            
