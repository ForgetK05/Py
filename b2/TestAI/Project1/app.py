from flask import Flask, render_template, request, jsonify
import sympy

app = Flask(__name__)


# Route 1: Chỉ phục vụ trang web (giao diện)
@app.route('/')
def index():
    # Chỉ trả về tệp HTML, không tính toán gì ở đây
    return render_template('index.html')


# Route 2: API để giải toán (sẽ được JavaScript gọi)
@app.route('/solve', methods=['POST'])
def solve_equation():
    try:
        # Lấy dữ liệu JSON mà JavaScript gửi lên
        data = request.json
        expression = data['expression']
        variable = data['variable']

        x = sympy.symbols(variable)

        # Giải phương trình
        expr = sympy.sympify(expression)
        solutions = sympy.solve(expr, x)

        # Chuyển kết quả sang chuỗi LaTeX
        solution_latex = sympy.latex(solutions)

        # Trả về kết quả dưới dạng JSON
        return jsonify({'success': True, 'solution': solution_latex})

    except Exception as e:
        # Trả về lỗi nếu có
        return jsonify({'success': False, 'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)