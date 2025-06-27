from obsidian.acquisition import aq_class_dict, aq_hp_defaults

# Manually choose the acquisition function
selected_aq = 'EI'  # Change this to 'UCB', 'PI', etc., as needed

# Retrieve the function associated with this choice
aq_function = aq_class_dict[selected_aq]  

# Retrieve any default hyperparameters (if they exist)
aq_params = {
    'acq_func': aq_function,
    **{param: details['val'] for param, details in aq_hp_defaults.get(selected_aq, {}).items()}
}

print(aq_params)  # Debugging: Check what parameters are selected