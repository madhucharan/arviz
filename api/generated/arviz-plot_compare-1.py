import arviz as az
model_compare = az.compare({'Centered 8 schools': az.load_arviz_data('centered_eight'),
                 'Non-centered 8 schools': az.load_arviz_data('non_centered_eight')})
az.plot_compare(model_compare)
