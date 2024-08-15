# CantoneseLM_survey 【三个链接+中文md】

[![evaluation](https://img.shields.io/badge/OpenCompass-Support-royalblue.svg
)](https://github.com/internLM/OpenCompass/) [![evaluation](https://img.shields.io/badge/lm--evaluation--harness-Support-blue
)](https://github.com/EleutherAI/lm-evaluation-harness)

<p align="center"> <img src="fig/banner.jpg" style="width: 100%;" id="title-icon">       </p>

<h4 align="center">
    <p>
        <b>简体中文</b>|
        <a href="https://github.com/jiangjyjy/CantoneseLM_survey">English</a>
    <p>
</h4>

<p align="center" style="display: flex; flex-direction: row; justify-content: center; align-items: center">
📄 <a href="https://arxiv.org/abs/xxxxx" target="_blank" style="margin-right: 15px; margin-left: 10px">论文</a> • 
🏆 <a href="https://github.com/haonan-li/xxx" target="_blank"  style="margin-left: 10px">排行榜</a> •
🤗 <a href="https://huggingface.co/datasets/xxx" target="_blank" style="margin-left: 10px">数据集</a> 
</p>

## Introduction

“广东话基准”是专为全球8500多万人使用的广东话设计的一种新的评估工具。随着自然语言处理领域的不断发展，对针对特定语言的健壮评估工具的需求变得越来越重要。为了解决现有粤语基准测试的巨大差距，该基准测试由四个不同的任务(Can-truthfulQA、Can-GSM8K、Can-ARC-C、Can-MMLU)组成，旨在全面评估粤语专用和通用大型语言模型(llm)在事实生成、数学逻辑、复杂推理和一般知识领域的粤语能力。“广东话基准”为广东话法学硕士提供可靠及准确的评估工具，不但有助评估现有的模型，亦有助未来广东话自然语言处理的研究和发展。
 
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
│       ├── Cant-ARC-C
│       ├── Cant-GSM8K
│       ├── Cant-MMLU
│       ├── Cant-TRANS
│       └── Cant-TruthfulQA
├── fig
│   ├── banner.jpg
│   └── logo.jpg
├── results&src
│   ├── ARC_c
│   │   ├── ARC-eval
│   │   └── ARC_c-yue
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

下表显示不同粤语基准(Cant-TruthfulQA, Cant-GSM8K, Cant-ARC-C, Cant-MMLU)在五样本和零样本设定下的表现。
<details>
<summary>Cant-TruthfulQA</summary>
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
        <td>--</td>
        <td>31.73</td>
        <td>19.53</td>
        <td>70.87</td>
        <td>--</td>
    </tr>
    <tr>
        <td>Qwen-2-7b</td>
        <td>13.27</td>
        <td>10.00</td>
        <td>66.14</td>
        <td>--</td>
        <td>16.91</td>
        <td>11.48</td>
        <td>67.71</td>
        <td>--</td>
    </tr>
    <tr>
        <td>Qwen-2-72b</td>
        <td>10.86</td>
        <td>9.68</td>
        <td>65.62</td>
        <td>--</td>
        <td>17.52</td>
        <td>12.38</td>
        <td>67.72</td>
        <td>--</td>
    </tr>
    <tr>
        <td>Mixtral-8x22b</td>
        <td>14.74</td>
        <td>10.83</td>
        <td>66.72</td>
        <td>--</td>
        <td>20.40</td>
        <td>14.09</td>
        <td>68.05</td>
        <td>--</td>
    </tr>
    <tr>
        <td>Mixtral-large-2</td>
        <td>19.72</td>
        <td>13.01</td>
        <td>69.06</td>
        <td>--</td>
        <td>31.38</td>
        <td>18.61</td>
        <td>72.07</td>
        <td>--</td>
    </tr>
    <tr>
        <td>Llama-3-8b</td>
        <td>8.40</td>
        <td>8.68</td>
        <td>64.37</td>
        <td>--</td>
        <td>28.68</td>
        <td>16.43</td>
        <td>70.82</td>
        <td>--</td>
    </tr>
    <tr>
        <td>Llama-3-70b</td>
        <td>10.98</td>
        <td>9.51</td>
        <td>66.10</td>
        <td>--</td>
        <td>33.06</td>
        <td>19.31</td>
        <td>71.95</td>
        <td>--</td>
    </tr>
    <tr>
        <td>Llama-3.1-8b</td>
        <td>13.82</td>
        <td>10.33</td>
        <td>66.97</td>
        <td>--</td>
        <td>26.18</td>
        <td>15.20</td>
        <td>70.28</td>
        <td>--</td>
    </tr>
    <tr>
        <td>Llama-3.1-70b</td>
        <td>21.03</td>
        <td>14.30</td>
        <td>68.31</td>
        <td>--</td>
        <td>34.72</td>
        <td>20.54</td>
        <td>70.80</td>
        <td>--</td>
    </tr>
    <tr>
        <td>Phi-3-medium</td>
        <td>18.70</td>
        <td>12.00</td>
        <td>67.36</td>
        <td>--</td>
        <td>22.00</td>
        <td>13.72</td>
        <td>67.57</td>
        <td>--</td>
    </tr>
    <tr>
        <td>Gemma-2-27b</td>
        <td>8.09</td>
        <td>8.44</td>
        <td>64.41</td>
        <td>--</td>
        <td>11.33</td>
        <td>9.98</td>
        <td>63.66</td>
        <td>--</td>
    </tr>
    <tr>
        <td>Yi-1.5-34b</td>
        <td>15.41</td>
        <td>11.11</td>
        <td>67.57</td>
        <td>--</td>
        <td>20.30</td>
        <td>13.20</td>
        <td>69.50</td>
        <td>--</td>
    </tr>
    <tr>
        <td>Internlm-2.5-7b</td>
        <td>14.46</td>
        <td>10.53</td>
        <td>63.48</td>
        <td>--</td>
        <td>22.30</td>
        <td>14.08</td>
        <td>67.61</td>
        <td>--</td>
    </tr>
    <tr>
        <td>ERNIE-Lite</td>
        <td>20.58</td>
        <td>12.23</td>
        <td>67.64</td>
        <td>--</td>
        <td>20.69</td>
        <td>12.27</td>
        <td>68.45</td>
        <td>--</td>
    </tr>
    <tr>
        <td>ERNIE-Tiny</td>
        <td>27.16</td>
        <td>14.49</td>
        <td>68.45</td>
        <td>--</td>
        <td>27.91</td>
        <td>15.28</td>
        <td>68.84</td>
        <td>--</td>
    </tr>
    <tr>
        <td>ERNIE-Speed</td>
        <td>22.58</td>
        <td>13.15</td>
        <td>67.84</td>
        <td>--</td>
        <td>23.61</td>
        <td>13.82</td>
        <td>68.27</td>
        <td>--</td>
    </tr>
    <tr>
        <td>ERNIE-Turbo</td>
        <td>17.91</td>
        <td>11.30</td>
        <td>66.71</td>
        <td>--</td>
        <td>21.19</td>
        <td>12.19</td>
        <td>68.29</td>
        <td>--</td>
    </tr>
    <tr>
        <td>Sensechat-5</td>
        <td>24.75</td>
        <td>15.11</td>
        <td>68.43</td>
        <td>--</td>
        <td>32.45</td>
        <td>19.70</td>
        <td>70.02</td>
        <td>--</td>
    </tr>
    <tr>
        <td>Claude-3.5</td>
        <td>14.23</td>
        <td>9.95</td>
        <td>67.56</td>
        <td>--</td>
        <td>12.66</td>
        <td>10.06</td>
        <td>68.12</td>
        <td>--</td>
    </tr>
    <tr>
        <td>GLM-4</td>
        <td>13.44</td>
        <td>10.07</td>
        <td>67.26</td>
        <td>--</td>
        <td>23.57</td>
        <td>14.28</td>
        <td>70.30</td>
        <td>--</td>
    </tr>
    <tr>
        <td>ChatGPT</td>
        <td>25.07</td>
        <td>14.81</td>
        <td>67.78</td>
        <td>--</td>
        <td>31.84</td>
        <td>18.42</td>
        <td>70.41</td>
        <td>--</td>
    </tr>
    <tr>
        <td>GPT-4o</td>
        <td>17.58</td>
        <td>12.17</td>
        <td>68.68</td>
        <td>--</td>
        <td>27.64</td>
        <td>16.52</td>
        <td>71.59</td>
        <td>--</td>
    </tr>
    <tr>
        <td>GPT-4</td>
        <td>19.47</td>
        <td>13.45</td>
        <td>68.99</td>
        <td>--</td>
        <td>28.43</td>
        <td>16.74</td>
        <td>71.26</td>
        <td>--</td>
    </tr>
</table>
</details>

<details>
<summary>Cant-GSM8k</summary>
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
<summary>Cant-ARC-Challenge</summary>
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

## How to submit

* 对于开源/API模型，打开pull request来更新结果(你也可以在`results&src`文件夹中提供测试代码)。
* 对于非开源/API模型，在相应部分更新结果并打开pull请求。

## Data [hf?]
我们根据每个主题在[data](data)目录中提供了开发和测试数据集。您也可以通过[Hugging Face](https://huggingface.co/datasets/haonan-li/cmmlu)。

#### Quick Use [需要吗？]

我们的数据集已经添加到 [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) 和 [OpenCompass](https://github.com/InternLM/opencompass) 中，您可以通过这些开源平台快速测试。


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





## Citation 【填词符】
```
xxxx
```

## License[证书存疑]

The CantoneseLM_survey dataset is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).
