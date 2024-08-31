# CantoneseLM_survey

<!-- [![evaluation](https://img.shields.io/badge/OpenCompass-Support-royalblue.svg
)](https://github.com/internLM/OpenCompass/) [![evaluation](https://img.shields.io/badge/lm--evaluation--harness-Support-blue
)](https://github.com/EleutherAI/lm-evaluation-harness) -->

[![Python](https://img.shields.io/badge/python-3.10-blue?logo=python&logoColor=FED643)](https://www.python.org/downloads/release/python-395/)
[![Pytorch](https://img.shields.io/badge/pytorch-2.3.0-red?logo=pytorch)](https://pytorch.org/get-started/previous-versions/)

<p align="center"> <img src="fig/banner.png" style="width: 100%;" id="title-icon">       </p>

<h4 align="center">
    <p>
        <b>简体中文</b>|
        <a href="https://github.com/jiangjyjy/CantoneseLM_survey">English</a>
    <p>
</h4>

<p align="center" style="display: flex; flex-direction: row; justify-content: center; align-items: center">
📄 <a href="https://arxiv.org/abs/xxxxx" target="_blank" style="margin-right: 15px; margin-left: 10px">论文</a> • 
🏆 <a href="https://github.com/haonan-li/xxx" target="_blank"  style="margin-left: 10px">排行榜</a> 
</p>

## Introduction

随着大型语言模型（LLMs）的迅速发展，如GPT-X和Llama-X，自然语言处理（NLP）技术取得了显著进步，但这些进展主要集中在英语和少数数据资源丰富的语言上，像粤语这种有着全球超过8500万使用者的语言却被忽视。尽管粤语使用地区和全球粤语社群在经济上具有重要性，粤语的技术发展，特别是在LLM领域，依然十分有限，大部分研究成果仍然是闭源的且发展不足。为了解决这一差距，我们系统性地回顾了现有的粤语NLP技术，包括谣言检测、情感分析和机器翻译等，并引入了新的基准测试 (Yue-TruthfulQA、Yue-GSM8K、Yue-ARC-C、Yue-MMLU和Yue-TRANS)，以评估LLM在粤语各个维度上的能力。这些基准测试由英语或普通话翻译而来，并经过人工校对，为粤语专用和通用LLM的全面评估提供了依据。我们对23个模型的分析揭示了现存的差距，并提出了未来研究的潜在方向，强调了加强粤语LLM开发的重要性，以满足这一重要群体的语言和文化需求。
 
<p align="center">  <img src="fig/logo.jpg" style="width: 95%;" id="title-icon"> </p>

## Files
```bash
.
├── README.md
├── README_CN.md
├── data
│   ├── historical_data
│   │   └── 2024-07-20
│   └── latest_data
│       ├── Yue-ARC-C
│       ├── Yue-GSM8K
│       ├── Yue-MMLU
│       ├── Yue-TRANS
│       └── Yue-TruthfulQA
├── fig
│   ├── banner.png
│   └── logo.jpg
├── results&src
│   ├── ARC_c
│   │   ├── ARC-eval
│   │   ├── ARC_c-en
│   │   └── ARC_c-yue
│   ├── CMMLU
│   │   ├── CMMLU-yue
│   │   └── CMMLU-zh
│   ├── GSM8K
│   │   ├── GSM8K-en
│   │   ├── GSM8K-eval
│   │   └── GSM8K-yue
│   ├── Translation
│   │   ├── Infer-Time.xlsx
│   │   ├── evaluation
│   │   └── prediction
│   └── TruthfulQA
│       ├── TruthfulQA-en
│       ├── TruthfulQA-eval
│       └── TruthfulQA-yue
└── script
    ├── arc_example.sh
    ├── gsm8k_example.sh
    ├── translation_example.sh
    └── truthfulqa_example.sh
```

## Leaderboard

下表显示不同粤语基准(Yue-TruthfulQA, Yue-GSM8K, Yue-ARC-C, Yue-MMLU)在五样本和零样本设定下的表现。
<details>
<summary>Yue-TruthfulQA</summary>
<table>
    <tr>
        <th rowspan=2>Models</th>
        <th colspan=4>0-shot (correct)</th>
        <th colspan=4>5-shot (correct)</th>
    </tr>
    <tr>
        <th>Rouge-l</th>
        <th>Bleu-4</th>
        <th>BERTScore</th>
        <th>Human</th>
        <th>Rouge-l</th>
        <th>Bleu-4</th>
        <th>BERTScore</th>
        <th>Human</th>
    </tr>
    <tr>
        <td>Qwen-1.5-110b</td>
        <td>26.04</td>
        <td>15.95</td>
        <td>69.29</td>
        <td>4.02</td>
        <td>31.73</td>
        <td>19.53</td>
        <td>70.87</td>
        <td>4.03</td>
    </tr>
    <tr>
        <td>Qwen-2-7b</td>
        <td>13.27</td>
        <td>10.00</td>
        <td>66.14</td>
        <td>3.23</td>
        <td>16.91</td>
        <td>11.48</td>
        <td>67.71</td>
        <td>3.35</td>
    </tr>
    <tr>
        <td>Qwen-2-72b</td>
        <td>10.86</td>
        <td>9.68</td>
        <td>65.62</td>
        <td>3.25</td>
        <td>17.52</td>
        <td>12.38</td>
        <td>67.72</td>
        <td>3.61</td>
    </tr>
    <tr>
        <td>Mixtral-8x22b</td>
        <td>14.74</td>
        <td>10.83</td>
        <td>66.72</td>
        <td>3.40</td>
        <td>20.40</td>
        <td>14.09</td>
        <td>68.05</td>
        <td>3.85</td>
    </tr>
    <tr>
        <td>Mixtral-large-2</td>
        <td>19.72</td>
        <td>13.01</td>
        <td>69.06</td>
        <td>3.96</td>
        <td>31.38</td>
        <td>18.61</td>
        <td>72.07</td>
        <td>4.20</td>
    </tr>
    <tr>
        <td>Llama-3-8b</td>
        <td>8.40</td>
        <td>8.68</td>
        <td>64.37</td>
        <td>3.20</td>
        <td>28.68</td>
        <td>16.43</td>
        <td>70.82</td>
        <td>4.04</td>
    </tr>
    <tr>
        <td>Llama-3-70b</td>
        <td>10.98</td>
        <td>9.51</td>
        <td>66.10</td>
        <td>3.87</td>
        <td>33.06</td>
        <td>19.31</td>
        <td>71.95</td>
        <td>4.15</td>
    </tr>
    <tr>
        <td>Llama-3.1-8b</td>
        <td>13.82</td>
        <td>10.33</td>
        <td>66.97</td>
        <td>3.52</td>
        <td>26.18</td>
        <td>15.20</td>
        <td>70.28</td>
        <td>3.98</td>
    </tr>
    <tr>
        <td>Llama-3.1-70b</td>
        <td>21.03</td>
        <td>14.30</td>
        <td>68.31</td>
        <td>4.05</td>
        <td>34.72</td>
        <td>20.54</td>
        <td>70.80</td>
        <td>4.10</td>
    </tr>
    <tr>
        <td>Phi-3-medium</td>
        <td>18.70</td>
        <td>12.00</td>
        <td>67.36</td>
        <td>3.54</td>
        <td>22.00</td>
        <td>13.72</td>
        <td>67.57</td>
        <td>3.49</td>
    </tr>
    <tr>
        <td>Gemma-2-27b</td>
        <td>8.09</td>
        <td>8.44</td>
        <td>64.41</td>
        <td>3.28</td>
        <td>11.33</td>
        <td>9.98</td>
        <td>63.66</td>
        <td>3.21</td>
    </tr>
    <tr>
        <td>Yi-1.5-34b</td>
        <td>15.41</td>
        <td>11.11</td>
        <td>67.57</td>
        <td>3.60</td>
        <td>20.30</td>
        <td>13.20</td>
        <td>69.50</td>
        <td>3.92</td>
    </tr>
    <tr>
        <td>Internlm-2.5-7b</td>
        <td>14.46</td>
        <td>10.53</td>
        <td>63.48</td>
        <td>3.10</td>
        <td>22.30</td>
        <td>14.08</td>
        <td>67.61</td>
        <td>3.67</td>
    </tr>
    <tr>
        <td>ERNIE-Lite</td>
        <td>20.58</td>
        <td>12.23</td>
        <td>67.64</td>
        <td>3.44</td>
        <td>20.69</td>
        <td>12.27</td>
        <td>68.45</td>
        <td>3.62</td>
    </tr>
    <tr>
        <td>ERNIE-Tiny</td>
        <td>27.16</td>
        <td>14.49</td>
        <td>68.45</td>
        <td>3.48</td>
        <td>27.91</td>
        <td>15.28</td>
        <td>68.84</td>
        <td>3.68</td>
    </tr>
    <tr>
        <td>ERNIE-Speed</td>
        <td>22.58</td>
        <td>13.15</td>
        <td>67.84</td>
        <td>3.48</td>
        <td>23.61</td>
        <td>13.82</td>
        <td>68.27</td>
        <td>3.62</td>
    </tr>
    <tr>
        <td>ERNIE-Turbo</td>
        <td>17.91</td>
        <td>11.30</td>
        <td>66.71</td>
        <td>3.40</td>
        <td>21.19</td>
        <td>12.19</td>
        <td>68.29</td>
        <td>3.60</td>
    </tr>
    <tr>
        <td>Sensechat-5</td>
        <td>24.75</td>
        <td>15.11</td>
        <td>68.43</td>
        <td>3.72</td>
        <td>32.45</td>
        <td>19.70</td>
        <td>70.02</td>
        <td>3.96</td>
    </tr>
    <tr>
        <td>Claude-3.5</td>
        <td>14.23</td>
        <td>9.95</td>
        <td>67.56</td>
        <td>3.92</td>
        <td>12.66</td>
        <td>10.06</td>
        <td>68.12</td>
        <td>4.07</td>
    </tr>
    <tr>
        <td>GLM-4</td>
        <td>13.44</td>
        <td>10.07</td>
        <td>67.26</td>
        <td>3.74</td>
        <td>23.57</td>
        <td>14.28</td>
        <td>70.30</td>
        <td>4.08</td>
    </tr>
    <tr>
        <td>ChatGPT</td>
        <td>25.07</td>
        <td>14.81</td>
        <td>67.78</td>
        <td>3.98</td>
        <td>31.84</td>
        <td>18.42</td>
        <td>70.41</td>
        <td>4.02</td>
    </tr>
    <tr>
        <td>GPT-4o</td>
        <td>17.58</td>
        <td>12.17</td>
        <td>68.68</td>
        <td>3.98</td>
        <td>27.64</td>
        <td>16.52</td>
        <td>71.59</td>
        <td>4.05</td>
    </tr>
    <tr>
        <td>GPT-4</td>
        <td>19.47</td>
        <td>13.45</td>
        <td>68.99</td>
        <td>4.10</td>
        <td>28.43</td>
        <td>16.74</td>
        <td>71.26</td>
        <td>4.20</td>
    </tr>
</table>
</details>

<details>
<summary>Yue-GSM8k</summary>
<table>
    <tr>
        <th>Models</th>
        <th>Accuracy (0-shot)</th>
        <th>Accuracy (5-shot)</th>
    </tr>
    <tr>
        <td>Qwen-1.5-110b</td>
        <td>52.77</td>
        <td>58.68</td>
    </tr>
    <tr>
        <td>Qwen-2-7b</td>
        <td>50.72</td>
        <td>62.40</td>
    </tr>
    <tr>
        <td>Qwen-2-72b</td>
        <td>78.62</td>
        <td>78.47</td>
    </tr>
    <tr>
        <td>Mixtral-8x22b</td>
        <td>63.08</td>
        <td>66.41</td>
    </tr>
    <tr>
        <td>Mixtral-large-2</td>
        <td>78.01</td>
        <td>81.43</td>
    </tr>
    <tr>
        <td>Llama-3-8b</td>
        <td>52.16</td>
        <td>49.81</td>
    </tr>
    <tr>
        <td>Llama-3-70b</td>
        <td>71.04</td>
        <td>75.97</td>
    </tr>
    <tr>
        <td>Llama-3.1-8b</td>
        <td>63.91</td>
        <td>61.56</td>
    </tr>
    <tr>
        <td>Llama-3.1-70b</td>
        <td>51.93</td>
        <td>79.15</td>
    </tr>
    <tr>
        <td>Phi-3-medium</td>
        <td>56.79</td>
        <td>63.31</td>
    </tr>
    <tr>
        <td>Gemma-2-27b</td>
        <td>9.40</td>
        <td>3.64</td>
    </tr>
    <tr>
        <td>Yi-1.5-34b</td>
        <td>67.63</td>
        <td>69.75</td>
    </tr>
    <tr>
        <td>Internlm-2.5-7b</td>
        <td>55.72</td>
        <td>43.90</td>
    </tr>
    <tr>
        <td>ERNIE-turbo</td>
        <td>13.80</td>
        <td>10.54</td>
    </tr>
    <tr>
        <td>ERNIE-Speed</td>
        <td>26.69</td>
        <td>26.99</td>
    </tr>
    <tr>
        <td>ERNIE-Lite</td>
        <td>52.84</td>
        <td>31.46</td>
    </tr>
    <tr>
        <td>ERNIE-Tiny</td>
        <td>3.72</td>
        <td>4.55</td>
    </tr>
    <tr>
        <td>SenseChat-5</td>
        <td>77.48</td>
        <td>73.16</td>
    </tr>
    <tr>
        <td>Claude-3.5</td>
        <td>66.11</td>
        <td>68.31</td>
    </tr>
    <tr>
        <td>GLM-4</td>
        <td>76.42</td>
        <td>77.10</td>
    </tr>
    <tr>
        <td>ChatGPT</td>
        <td>22.14</td>
        <td>41.09</td>
    </tr>
    <tr>
        <td>GPT-4o</td>
        <td>81.80</td>
        <td>83.47</td>
    </tr>
    <tr>
        <td>GPT-4</td>
        <td>79.23</td>
        <td>83.25</td>
    </tr>
</table>
</details>

<details>
<summary>Yue-ARC-Challenge</summary>
<table>
    <tr>
        <th>Models</th>
        <th>Accuracy (0-shot)</th>
        <th>Accuracy (5-shot)</th>
    </tr>
    <tr>
        <td>Qwen-1.5-110b</td>
        <td>88.64</td>
        <td>90.18</td>
    </tr>
    <tr>
        <td>Qwen-2-7b</td>
        <td>78.74</td>
        <td>80.10</td>
    </tr>
    <tr>
        <td>Qwen-2-72b</td>
        <td>90.69</td>
        <td>92.31</td>
    </tr>
    <tr>
        <td>Mixtral-8x22b</td>
        <td>75.92</td>
        <td>77.63</td>
    </tr>
    <tr>
        <td>Mixtral-large-2</td>
        <td>88.64</td>
        <td>90.44</td>
    </tr>
    <tr>
        <td>Llama-3-1.8b</td>
        <td>69.00</td>
        <td>67.21</td>
    </tr>
    <tr>
        <td>Llama-3-8b</td>
        <td>67.64</td>
        <td>52.69</td>
    </tr>
    <tr>
        <td>Llama-3-70b</td>
        <td>84.46</td>
        <td>84.97</td>
    </tr>
    <tr>
        <td>Llama-3.1-8b</td>
        <td>69.00</td>
        <td>67.21</td>
    </tr>
    <tr>
        <td>Llama-3.1-70b</td>
        <td>88.90</td>
        <td>88.39</td>
    </tr>
    <tr>
        <td>Phi-3-medium</td>
        <td>63.11</td>
        <td>78.14</td>
    </tr>
    <tr>
        <td>Gemma-2-27b</td>
        <td>67.55</td>
        <td>55.08</td>
    </tr>
    <tr>
        <td>Yi-1.5-34b</td>
        <td>84.71</td>
        <td>86.68</td>
    </tr>
    <tr>
        <td>ERNIE-turbo</td>
        <td>38.51</td>
        <td>44.24</td>
    </tr>
    <tr>
        <td>ERNIE-Speed</td>
        <td>74.04</td>
        <td>46.88</td>
    </tr>
    <tr>
        <td>ERNIE-Lite</td>
        <td>72.42</td>
        <td>77.28</td>
    </tr>
    <tr>
        <td>ERNIE-Tiny</td>
        <td>33.56</td>
        <td>30.15</td>
    </tr>
    <tr>
        <td>Internlm-2.5-7b</td>
        <td>80.79</td>
        <td>79.85</td>
    </tr>
    <tr>
        <td>SenseChat-5</td>
        <td>87.96</td>
        <td>87.28</td>
    </tr>
    <tr>
        <td>Claude-3.5</td>
        <td>91.63</td>
        <td>92.23</td>
    </tr>
    <tr>
        <td>GLM-4</td>
        <td>88.90</td>
        <td>88.64</td>
    </tr>
    <tr>
        <td>ChatGPT</td>
        <td>69.60</td>
        <td>70.79</td>
    </tr>
    <tr>
        <td>GPT-4o</td>
        <td>92.06</td>
        <td>94.28</td>
    </tr>
    <tr>
        <td>GPT-4</td>
        <td>92.74</td>
        <td>92.06</td>
    </tr>
</table>
</details>

<details>
<summary>Yue-CMMLU</summary>
<table>
    <tr>
        <th rowspan=2>Models</th>
        <th colspan=5>0-shot (correct)</th>
        <th colspan=5>5-shot (correct)</th>
    </tr>
    <tr>
        <td>STEM</td>
        <td>Hum.</td>
        <td>S.S.</td>
        <td>C.S.</td>
        <td>Oth.</td>
        <td>STEM</td>
        <td>Hum.</td>
        <td>S.S.</td>
        <td>C.S.</td>
        <td>Oth.</td>
    </tr>
    <tr>
        <td>Qwen1.5-110b</td>
        <td>80.41</td>
        <td>88.62</td>
        <td>82.26</td>
        <td>83.91</td>
        <td>75.77</td>
        <td>86.14</td>
        <td>91.3</td>
        <td>90.59</td>
        <td>90.62</td>
        <td>82.76</td>
    </tr>
    <tr>
        <td>Qwen-2-7b</td>
        <td>69.58</td>
        <td>80.7</td>
        <td>76.34</td>
        <td>79.76</td>
        <td>69.94</td>
        <td>74.14</td>
        <td>81.02</td>
        <td>79.82</td>
        <td>81.28</td>
        <td>75.19</td>
    </tr>
    <tr>
        <td>Qwen-2-72b</td>
        <td>80.21</td>
        <td>88.46</td>
        <td>87.00</td>
        <td>87.45</td>
        <td>80.16</td>
        <td>87.36</td>
        <td>91.86</td>
        <td>89.68</td>
        <td>91.98</td>
        <td>87.44</td>
    </tr>
    <tr>
        <td>Mixtral-8x22b</td>
        <td>43.68</td>
        <td>56.96</td>
        <td>48.4</td>
        <td>59.0</td>
        <td>50.52</td>
        <td>50.88</td>
        <td>59.78</td>
        <td>57.84</td>
        <td>62.79</td>
        <td>58.82</td>
    </tr>
    <tr>
        <td>Mixtral-large-2</td>
        <td>60.19</td>
        <td>76.08</td>
        <td>70.74</td>
        <td>74.92</td>
        <td>60.38</td>
        <td>63.84</td>
        <td>79.65</td>
        <td>71.66</td>
        <td>78.84</td>
        <td>68.5</td>
    </tr>
    <tr>
        <td>Llama-3-8b</td>
        <td>47.69</td>
        <td>59.16</td>
        <td>53.72</td>
        <td>56.6</td>
        <td>49.42</td>
        <td>46.24</td>
        <td>58.33</td>
        <td>52.55</td>
        <td>53.94</td>
        <td>43.1</td>
    </tr>
    <tr>
        <td>Llama-3-70b</td>
        <td>58.33</td>
        <td>73.04</td>
        <td>71.92</td>
        <td>74.86</td>
        <td>63.89</td>
        <td>57.34</td>
        <td>72.79</td>
        <td>72.95</td>
        <td>73.07</td>
        <td>63.65</td>
    </tr>
    <tr>
        <td>Llama-3.1-8b</td>
        <td>44.86</td>
        <td>58.27</td>
        <td>53.7</td>
        <td>56.08</td>
        <td>45.96</td>
        <td>46.01</td>
        <td>58.06</td>
        <td>54.02</td>
        <td>58.31</td>
        <td>53.16</td>
    </tr>
    <tr>
        <td>Llama-3.1-70b</td>
        <td>60.96</td>
        <td>76.43</td>
        <td>73.38</td>
        <td>76.93</td>
        <td>67.04</td>
        <td>64.0</td>
        <td>78.13</td>
        <td>74.9</td>
        <td>78.14</td>
        <td>71.82</td>
    </tr>
    <tr>
        <td>Phi-3-medium</td>
        <td>45.65</td>
        <td>61.53</td>
        <td>51.14</td>
        <td>58.13</td>
        <td>44.86</td>
        <td>45.65</td>
        <td>59.24</td>
        <td>53.02</td>
        <td>59.31</td>
        <td>49.18</td>
    </tr>
    <tr>
        <td>Gemma-2-27b</td>
        <td>37.68</td>
        <td>53.94</td>
        <td>49.2</td>
        <td>53.46</td>
        <td>47.5</td>
        <td>33.55</td>
        <td>40.98</td>
        <td>44.88</td>
        <td>43.75</td>
        <td>40.72</td>
    </tr>
    <tr>
        <td>Yi-1.5-34b</td>
        <td>70.73</td>
        <td>81.46</td>
        <td>79.57</td>
        <td>81.54</td>
        <td>68.47</td>
        <td>78.2</td>
        <td>85.15</td>
        <td>80.49</td>
        <td>83.52</td>
        <td>74.13</td>
    </tr>
    <tr>
        <td>Internlm-2.5-7b</td>
        <td>66.93</td>
        <td>78.74</td>
        <td>73.38</td>
        <td>73.42</td>
        <td>63.64</td>
        <td>70.47</td>
        <td>80.84</td>
        <td>75.19</td>
        <td>76.79</td>
        <td>64.63</td>
    </tr>
    <tr>
        <td>ERNIE-Lite</td>
        <td>60.73</td>
        <td>67.56</td>
        <td>61.02</td>
        <td>67.73</td>
        <td>53.04</td>
        <td>62.43</td>
        <td>70.27</td>
        <td>64.84</td>
        <td>71.55</td>
        <td>60.04</td>
    </tr>
    <tr>
        <td>ERNIE-Tiny</td>
        <td>33.24</td>
        <td>37.86</td>
        <td>32.3</td>
        <td>37.88</td>
        <td>34.36</td>
        <td>32.68</td>
        <td>38.79</td>
        <td>34.6</td>
        <td>37.66</td>
        <td>32.52</td>
    </tr>
    <tr>
        <td>ERNIE-turbo</td>
        <td>50.7</td>
        <td>54.62</td>
        <td>45.62</td>
        <td>53.53</td>
        <td>41.82</td>
        <td>49.33</td>
        <td>57.66</td>
        <td>46.76</td>
        <td>54.28</td>
        <td>41.42</td>
    </tr>
    <tr>
        <td>Sensechat-5</td>
        <td>73.86</td>
        <td>83.21</td>
        <td>76.95</td>
        <td>80.73</td>
        <td>69.56</td>
        <td>73.52</td>
        <td>82.0</td>
        <td>74.78</td>
        <td>79.88</td>
        <td>68.57</td>
    </tr>
    <tr>
        <td>Claude-3.5</td>
        <td>60.6</td>
        <td>72.67</td>
        <td>75.98</td>
        <td>76.63</td>
        <td>64.6</td>
        <td>59.02</td>
        <td>81.24</td>
        <td>82.54</td>
        <td>83.08</td>
        <td>75.51</td>
    </tr>
    <tr>
        <td>GLM-4</td>
        <td>75.66</td>
        <td>84.39</td>
        <td>75.75</td>
        <td>80.17</td>
        <td>64.23</td>
        <td>76.0</td>
        <td>84.2</td>
        <td>78.06</td>
        <td>80.07</td>
        <td>71.77</td>
    </tr>
    <tr>
        <td>ChatGPT</td>
        <td>44.58</td>
        <td>57.72</td>
        <td>52.42</td>
        <td>58.74</td>
        <td>49.78</td>
        <td>41.52</td>
        <td>56.34</td>
        <td>54.54</td>
        <td>60.33</td>
        <td>59.87</td>
    </tr>
    <tr>
        <td>GPT-4o</td>
        <td>71.72</td>
        <td>83.28</td>
        <td>84.32</td>
        <td>84.12</td>
        <td>74.16</td>
        <td>72.87</td>
        <td>85.03</td>
        <td>81.59</td>
        <td>84.32</td>
        <td>71.53</td>
    </tr>
    <tr>
        <td>GPT-4</td>
        <td>60.28</td>
        <td>75.38</td>
        <td>74.46</td>
        <td>77.26</td>
        <td>67.28</td>
        <td>63.5</td>
        <td>76.75</td>
        <td>74.57</td>
        <td>77.56</td>
        <td>70.78</td>
    </tr>
</table>
</details>

## How to submit

* 对于开源/API模型，打开pull request来更新结果(你也可以在`results&src`文件夹中提供测试代码)。
* 对于非开源/API模型，在相应部分更新结果并打开pull请求。

## Data 
我们根据每个主题在[data](data)目录中提供了开发和测试数据集。

<!-- #### Quick Use

我们的数据集已经添加到 [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) 和 [OpenCompass](https://github.com/InternLM/opencompass) 中，您可以通过这些开源平台快速测试。 -->


#### Data Format
Each question in the dataset is a multiple-choice questions with 4 choices and only one choice as the correct answer.  The data is json file, which is the same format as the original. Here is an example:
```json
    {
        "id": "Mercury_7175875",
        "question": "一個天文學家觀察到一個行星喺隕石碰撞後旋轉得更快。呢個旋轉增加最有可能嘅影響係乜嘢？",
        "A": "行星嘅密度會減少。",
        "B": "行星嘅年會變得更長。",
        "C": "行星嘅日會變得更短。",
        "D": "行星嘅重力會變得更強。",
        "answer": "C",
        "no": 1
    }
```


#### Evaluation
The code for evaluation of each model we used is in [src](results&src), and the code examples to run them is listed in [script](script) directory.

For example,
```bash
cd script
bash arc_example.sh
```





## Citation 
```
@misc{jiang2024farcantonesenlpgo,
      title={How Far Can Cantonese NLP Go? Benchmarking Cantonese Capabilities of Large Language Models}, 
      author={Jiyue Jiang and Liheng Chen and Pengan Chen and Sheng Wang and Qinghang Bao and Lingpeng Kong and Yu Li and Chuan Wu},
      year={2024},
      eprint={2408.16756},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2408.16756}, 
}
```


