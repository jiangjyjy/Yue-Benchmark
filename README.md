# CantoneseLM_survey 【三个链接+中文md】

[![evaluation](https://img.shields.io/badge/OpenCompass-Support-royalblue.svg
)](https://github.com/internLM/OpenCompass/) [![evaluation](https://img.shields.io/badge/lm--evaluation--harness-Support-blue
)](https://github.com/EleutherAI/lm-evaluation-harness)

<p align="center"> <img src="fig/banner.jpg" style="width: 100%;" id="title-icon">       </p>

<h4 align="center">
    <p>
        <a href="https://github.com/jiangjyjy/CantoneseLM_survey">简体中文</a> |
        <b>English</b> 
    <p>
</h4>

<p align="center" style="display: flex; flex-direction: row; justify-content: center; align-items: center">
📄 <a href="https://arxiv.org/abs/xxxxx" target="_blank" style="margin-right: 15px; margin-left: 10px">Paper</a> • 
🏆 <a href="https://github.com/haonan-li/xxx" target="_blank"  style="margin-left: 10px">Leaderboard</a> •
🤗 <a href="https://huggingface.co/datasets/xxx" target="_blank" style="margin-left: 10px">Dataset</a> 
</p>

## Introduction

The Cantonese Benchmark is a new evaluation tool specifically designed for Cantonese, a language spoken by over 85 million people worldwide. As the field of natural language processing continues to grow, the need for robust evaluation tools tailored to specific languages becomes increasingly important. Addressing the significant gap in available benchmarks for Cantonese, this benchmark is composed of four distinct tasks (Cant-Truthful, Cant-GSM8K, Cant-ARC-C, Cant-MMLU), aiming to comprehensively evaluate the Cantonese capabilities of both Cantonese-specific and general-purpose large language models (LLMs) in the areas of factual generation, mathematical logic, complex reasoning, and general knowledge. By providing a reliable and accurate evaluation tool for Cantonese LLMs, the Cantonese Benchmark will not only facilitate the assessment of current models but also pave the way for future research and advancements in Cantonese natural language processing.
<p align="center">  <img src="fig/logo.jpg" style="width: 95%;" id="title-icon"> </p>

## Leaderboard

The following tables display the performance of models on different cantonese benchmarks (Cant-Truthful, Cant-GSM8K, Cant-ARC-C, Cant-MMLU) in the five-shot and zero-shot settings. 
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

* For open-source/API models, open pull request to update the result (you can also provide test code in `src` folder).
* For not open-source/API models, update results in the cooresponding part and open pull request.

## Data
We provide our dataset according to each subject in [data](data) folder. You can also access our dataset via [Hugging Face](https://huggingface.co/datasets/haonan-li/cmmlu).

#### Quick Use

Our dataset has been added to [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) and [OpenCompass](https://github.com/InternLM/opencompass), you can evaluate your model via these open-source tools.

#### Data Format
Each question in the dataset is a multiple-choice questions with 4 choices and only one choice as the correct answer.  The data is comma saperated .csv file. Here is an example:
```
    同一物种的两类细胞各产生一种分泌蛋白，组成这两种蛋白质的各种氨基酸含量相同，但排列顺序不同。其原因是参与这两种蛋白质合成的,tRNA种类不同,同一密码子所决定的氨基酸不同,mRNA碱基序列不同,核糖体成分不同,C
    Translation:"Two types of cells within the same species each produce a secretion protein. The various amino acids that make up these two proteins have the same composition but differ in their arrangement. The reason for this difference in arrangement in the synthesis of these two proteins is,Different types of tRNA,Different amino acids determined by the same codon,Different mRNA base sequences,Different ribosome components,C"
```


#### Prompt
We provide the preprocessing code in [src/mp_utils](https://github.com/haonan-li/CMMLU/tree/master/src/mp_utils.py) directory. It includes apporach we used to generate direct answer prompt and chain-of-thought (COT) prompt.

Here is an example of data after adding direct answer prompt:
```
    以下是关于(高中生物)的单项选择题，请直接给出正确答案的选项。
    (Here are some single-choice questions about(high school biology), please provide the correct answer choice directly.)
    题目：同一物种的两类细胞各产生一种分泌蛋白，组成这两种蛋白质的各种氨基酸含量相同，但排列顺序不同。其原因是参与这两种蛋白质合成的：
    (Two types of cells within the same species each produce a secretion protein. The various amino acids that make up these two proteins have the same composition but differ in their arrangement. The reason for this difference in arrangement in the synthesis of these two proteins is)
    A. tRNA种类不同(Different types of tRNA)
    B. 同一密码子所决定的氨基酸不同(Different amino acids determined by the same codon)
    C. mRNA碱基序列不同(Different mRNA base sequences)
    D. 核糖体成分不同(Different ribosome components)
    答案是：C(Answer: C)

    ... [other examples] 

    题目：某种植物病毒V是通过稻飞虱吸食水稻汁液在水稻间传播的。稻田中青蛙数量的增加可减少该病毒在水稻间的传播。下列叙述正确的是：
    (Question: A certain plant virus, V, is transmitted between rice plants through the feeding of rice planthoppers. An increase in the number of frogs in the rice field can reduce the spread of this virus among the rice plants. The correct statement among the options provided would be)
    A. 青蛙与稻飞虱是捕食关系(Frogs and rice planthoppers have a predatory relationship)
    B. 水稻和病毒V是互利共生关系(Rice plants and virus V have a mutualistic symbiotic relationship)
    C. 病毒V与青蛙是寄生关系(Virus V and frogs have a parasitic relationship)
    D. 水稻与青蛙是竞争关系(Rice plants and frogs have a competitive relationship)
    答案是： (Answer:)
```
For the COT prompt we modified the prompt from“请直接给出正确答案的选项 (please provide the correct answer choice directly)” to “逐步分析并选出正确答案 (Analyze step by step and select the correct answer).”

#### Evaluation
The code for evaluation of each model we used is in [src](src), and the code to run them is listed in [script](script) directory.





## Citation 【填词符】
```
xxxx
```

## License[证书存疑]

The CantoneseLM_survey dataset is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).
