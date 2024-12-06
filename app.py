from flask import Flask, render_template, request, jsonify
from iching_core.hexagram_generator import HexagramGenerator
from iching_core.hexagram_analyzer import HexagramAnalyzer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        topic = data.get('topic', '')
        template = data.get('template', 'traditional')
        
        # 生成卦象
        generator = HexagramGenerator()
        hexagram = generator.generate_hexagram(topic)
        
        # 分析卦象
        analyzer = HexagramAnalyzer(hexagram)
        analysis_result = analyzer.generate_analysis()
        
        return jsonify({
            'success': True,
            'result': analysis_result
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)