# Handles requests and performs calculations.
from django.shortcuts import render

def math_form_view(request):
    # Displays the initial form.
    return render(request, 'math_operations/math_form.html')

def result_view(request):
    # Handles form submission and calculations.
    context = {}
    if request.method == 'POST':
        try:
            x = float(request.POST.get('x', '0'))
            y = float(request.POST.get('y', '0'))
            z = float(request.POST.get('z', '0'))

            context['original_x'] = x
            context['original_y'] = y
            context['original_z'] = z

            steps = [{'description': 'Initial value of x', 'value': x}]

            # Perform calculations (modifies x step-by-step).
            x += y
            steps.append({'description': 'After x += y', 'value': x})

            x -= z
            steps.append({'description': 'After x -= z', 'value': x})

            x *= y
            steps.append({'description': 'After x *= y', 'value': x})

            if z != 0:
                x %= z
                steps.append({'description': 'After x %= z', 'value': x})
            else:
                steps.append({'description': 'After x %= z', 'value': "Skipped (division by zero)"})

            if z != 0:
                x /= z
                steps.append({'description': 'After x /= z', 'value': x})
            else:
                steps.append({'description': 'After x /= z', 'value': "Skipped (division by zero)"})

            context['steps'] = steps
            context['final_x'] = x
            context['final_result'] = x + y + z  # Uses modified x + original y + z.

        except (ValueError, TypeError):
            context['error'] = "Invalid input. Please enter valid numbers."

    return render(request, 'math_operations/results.html', context)
