#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from datetime import datetime
from iching_core.hexagram_generator import HexagramGenerator
from iching_core.hexagram_analyzer import HexagramAnalyzer
from models.hexagram import Hexagram

def parse_args():
    parser = argparse.ArgumentParser(description='I Ching Analysis System')
    parser.add_argument('--topic', type=str, required=True,
                      help='The topic or question for divination')
    parser.add_argument('--output', type=str, default='analysis_result.md',
                      help='Output file path for the analysis result')
    parser.add_argument('--template', type=str, default='modern',
                      choices=['modern', 'traditional'],
                      help='Analysis template type')
    return parser.parse_args()

def generate_markdown(analysis_result: dict, template_type: str) -> str:
    """根据分析结果生成Markdown格式报告"""
    
    if template_type == 'modern':
        template = """# I Ching Analysis Report

## Basic Information
- Time: {time}
- Lunar Date: {lunar_date}
- Gan-Zhi: {gan_zhi}
- Topic: {topic}

## Hexagram Information
### Original Hexagram
- Name: {original_name}
- Trigrams: {original_trigrams}
- Text: {hexagram_text}
- Explanation: {original_explanation}

### Changed Hexagram
- Name: {changed_name}
- Trigrams: {changed_trigrams}
- Explanation: {changed_explanation}

## Analysis
### Relationships
#### World and Response
{shi_ying_analysis}

#### Five Elements
{wu_xing_analysis}

#### Six Relatives
{liu_qin_analysis}

## Recommendations
### Short Term
{short_term}

### Medium Term
{medium_term}

### Long Term
{long_term}

## Risk Assessment
{risk_assessment}
"""
    else:
        template = """# 周易卦象分析报告

## 基本信息
- 时间：{time}
- 农历：{lunar_date}
- 干支：{gan_zhi}
- 主题：{topic}

## 卦象信息
### 本卦
- 卦名：{original_name}
- 上下卦：{original_trigrams}
- 卦辞：{hexagram_text}
- 解释：{original_explanation}

### 变卦
- 卦名：{changed_name}
- 上下卦：{changed_trigrams}
- 解释：{changed_explanation}

## 分析
### 关系分析
#### 世应
{shi_ying_analysis}

#### 五行
{wu_xing_analysis}

#### 六亲
{liu_qin_analysis}

## 建议
### 近期
{short_term}

### 中期
{medium_term}

### 远期
{long_term}

## 风险评估
{risk_assessment}
"""

    # 从分析结果中提取数据
    basic_info = analysis_result['basic_info']
    hexagram_info = analysis_result['hexagram_info']
    relationships = analysis_result['relationships']
    recommendations = analysis_result['recommendations']

    # 格式化输出
    return template.format(
        time=basic_info['time'].strftime('%Y-%m-%d %H:%M:%S'),
        lunar_date=basic_info['lunar_date'],
        gan_zhi=basic_info['gan_zhi_info'],
        topic=basic_info['topic'],
        original_name=hexagram_info['original_hexagram_name'],
        original_trigrams=hexagram_info['original_trigrams'],
        hexagram_text=hexagram_info['hexagram_text'],
        original_explanation=hexagram_info['original_explanation'],
        changed_name=hexagram_info['changed_hexagram_name'],
        changed_trigrams=hexagram_info['changed_trigrams'],
        changed_explanation=hexagram_info['changed_explanation'],
        shi_ying_analysis=format_dict(relationships['shi_yao']),
        wu_xing_analysis=format_dict(relationships['wu_xing']),
        liu_qin_analysis=format_list(relationships['liu_qin']),
        short_term=format_list(recommendations['short_term']),
        medium_term=format_list(recommendations['medium_term']),
        long_term=format_list(recommendations['long_term']),
        risk_assessment=format_dict(recommendations['risks'])
    )

def format_dict(d: dict) -> str:
    """格式化字典为Markdown文本"""
    return '\n'.join([f'- {k}: {v}' for k, v in d.items()])

def format_list(l: list) -> str:
    """格式化列表为Markdown文本"""
    return '\n'.join([f'- {item}' for item in l])

def main():
    args = parse_args()
    
    # 生成卦象
    generator = HexagramGenerator()
    hexagram = generator.generate_hexagram(args.topic)
    
    # 分析卦象
    analyzer = HexagramAnalyzer(hexagram)
    analysis_result = analyzer.generate_analysis()
    
    # 生成报告
    report = generate_markdown(analysis_result, args.template)
    
    # 保存报告
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f'Analysis report has been saved to {args.output}')

if __name__ == '__main__':
    main()