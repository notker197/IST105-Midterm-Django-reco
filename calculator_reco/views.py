from django.shortcuts import render
from .forms import MathForm

def calculate_view(request):
    result = None
    error = None

    if request.method == 'POST':
        form = MathForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['input1']
            b = form.cleaned_data['input2']
            op = form.cleaned_data['operation']

            try:
                if op == 'power':
                    result = a ** b
                elif op == 'modulus':
                    if b == 0:
                        error = "Error: Modulus by zero"
                    else:
                        result = a % b
                elif op == 'average':
                    result = (a + b) / 2
                elif op == 'max':
                    result = max(a, b)

                if result is not None:
                    if result > 500:
                        result -= 100
                    if result % 2 == 0:
                        result /= 2

            except Exception as e:
                error = str(e)
    else:
        form = MathForm()

    return render(request, 'math_form.html', {'form': form, 'result': result, 'error': error})
