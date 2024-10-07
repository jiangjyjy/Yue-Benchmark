# How Far Can Cantonese NLP Go? Benchmarking Cantonese Capabilities of Large Language Models



[![Python](https://img.shields.io/badge/python-3.10-blue?logo=python&logoColor=FED643)](https://www.python.org/downloads/release/python-395/)
[![Pytorch](https://img.shields.io/badge/pytorch-2.3.0-red?logo=pytorch)](https://pytorch.org/get-started/previous-versions/)
[![evaluation](https://img.shields.io/badge/OpenCompass-Support-royalblue.svg)](https://github.com/internLM/OpenCompass/) 


<p align="center"> <img src="fig/banner.png" style="width: 100%;" id="title-icon">       </p>

<h4 align="center">
    <p>
        <a href="https://github.com/jiangjyjy/Yue-Benchmark/blob/main/README_CN.md">简体中文</a> |
        <b>English</b> 
    <p>
</h4>

<p align="center" style="display: flex; flex-direction: row; justify-content: center; align-items: center">
📄 <a href="https://arxiv.org/abs/2408.16756" target="_blank" style="margin-right: 15px; margin-left: 10px">Paper</a> • 
🏆 <a href="https://github.com/jiangjyjy/Yue-Benchmark/#Leaderboard" target="_blank"  style="margin-left: 10px">Leaderboard</a> 
•
🤗 <a href="https://huggingface.co/datasets/BillBao/Yue-Benchmark" target="_blank" style="margin-left: 10px">Dataset</a> 
</p>

## Introduction

The rapid evolution of large language models (LLMs), such as GPT-X and Llama-X, has driven significant advancements in NLP, yet much of this progress has centered on English and a few other well-resourced languages, leaving languages like Cantonese, spoken by over 85 million people worldwide, underrepresented. Despite the economic importance of Cantonese-speaking regions and communities globally, technological development for Cantonese, particularly in the realm of LLMs, remains limited, with most efforts closed-source and underdeveloped. To address this disparity, we systematically review existing Cantonese NLP technologies, including rumor detection, sentiment analysis, and machine translation, and introduce new benchmarks (Yue-TruthfulQA, Yue-GSM8K, Yue-ARC-C, Yue-MMLU, and Yue-TRANS) to evaluate LLMs' capabilities in Cantonese across various dimensions. These benchmarks, derived from English or Mandarin and manually verified, enable a comprehensive assessment of both Cantonese-specific and general-purpose LLMs. Our analysis of twenty-three models identifies gaps and potential directions for future research, emphasizing the need for enhanced Cantonese LLM development to meet the linguistic and cultural needs of this significant population.
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

The following tables display the performance of models on different cantonese benchmarks (Yue-Truthful, Yue-GSM8K, Yue-ARC-C, Yue-CMMLU) in the five-shot and zero-shot settings. 
<details>
<summary>Yue-TruthfulQA</summary>
<table>
    <tr>
        <th rowspan=2>Models</th>
        <th colspan=3>0-shot (correct)</th>
        <th colspan=3>5-shot (correct)</th>
    </tr>
    <tr>
        <th>Rouge-l</th>
        <th>Bleu-4</th>
        <th>BERTScore</th>
        <th>Rouge-l</th>
        <th>Bleu-4</th>
        <th>BERTScore</th>
    </tr>
    <tr>
        <td>Qwen-7b</td>
        <td>6.42</td>
        <td>3.99</td>
        <td>51.57</td>
        <td>4.02</td>
        <td>4.04</td>
        <td>2.98</td>
        <td>49.7</td>
        <td>4.03</td>
    </tr>
    <tr>
        <td>Qwen-1.5-7b</td>
        <td>20.54</td>
        <td>13.41</td>
        <td>66.45</td>
        <td>4.02</td>
        <td>12.45</td>
        <td>10.41</td>
        <td>61.59</td>
        <td>4.03</td>
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
        <td>Qwen-2.5-7b</td>
        <td>18.51</td>
        <td>12.28</td>
        <td>66.07</td>
        <td>3.25</td>
        <td>6.83</td>
        <td>8.07</td>
        <td>58.97</td>
        <td>3.61</td>
    </tr>
    <tr>
        <td>Qwen-2.5-72b</td>
        <td>13.03</td>
        <td>9.64</td>
        <td>66.94</td>
        <td>3.23</td>
        <td>20.23</td>
        <td>12.87</td>
        <td>69.53</td>
        <td>3.35</td>
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
        <td>Llama-2-7b</td>
        <td>3.48</td>
        <td>6.42</td>
        <td>57.16</td>
        <td>3.20</td>
        <td>3.57</td>
        <td>6.52</td>
        <td>56.36</td>
        <td>4.04</td>
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
        <td>Yi-6b</td>
        <td>1.37</td>
        <td>5.05</td>
        <td>53.16</td>
        <td>3.60</td>
        <td>1.07</td>
        <td>5.99</td>
        <td>54.21</td>
        <td>3.92</td>
    </tr>
    <tr>
        <td>Yi-1.5-6b</td>
        <td>1.21</td>
        <td>4.60</td>
        <td>42.15</td>
        <td>3.60</td>
        <td>1.04</td>
        <td>6.15</td>
        <td>53.85</td>
        <td>3.92</td>
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
        <td>Internlm-7b</td>
        <td>5.89</td>
        <td>6.65</td>
        <td>56.33</td>
        <td>3.10</td>
        <td>2.59</td>
        <td>3.68</td>
        <td>55.73</td>
        <td>3.67</td>
    </tr>
    <tr>
        <td>Internlm-7b-turbomind</td>
        <td>5.91</td>
        <td>6.71</td>
        <td>56.71</td>
        <td>3.10</td>
        <td>2.77</td>
        <td>3.82</td>
        <td>55.57</td>
        <td>3.67</td>
    </tr>
    <tr>
        <td>Internlm-2-7b</td>
        <td>7.93</td>
        <td>10.21</td>
        <td>63.81</td>
        <td>3.10</td>
        <td>17.66</td>
        <td>16.62</td>
        <td>33.33</td>
        <td>3.67</td>
    </tr>
    <tr>
        <td>Internlm-2-7b-chat</td>
        <td>6.7</td>
        <td>7.68</td>
        <td>61.83</td>
        <td>3.10</td>
        <td>3.3</td>
        <td>5.49</td>
        <td>65.47</td>
        <td>3.67</td>
    </tr>
    <tr>
        <td>Internlm-2-7b-turbomind</td>
        <td>8.09</td>
        <td>10.53</td>
        <td>64.3</td>
        <td>3.10</td>
        <td>17.69</td>
        <td>16.99</td>
        <td>63.68</td>
        <td>3.67</td>
    </tr>
    <tr>
        <td>Internlm-2.5-7b</td>
        <td>8.96</td>
        <td>10.53</td>
        <td>66.11</td>
        <td>3.10</td>
        <td>10.3</td>
        <td>14.47</td>
        <td>67.73</td>
        <td>3.67</td>
    </tr>
    <tr>
        <td>Internlm-2.5-7b-chat</td>
        <td>7.13</td>
        <td>8</td>
        <td>63.48</td>
        <td>3.10</td>
        <td>4.05</td>
        <td>7.19</td>
        <td>67.61</td>
        <td>3.67</td>
    </tr>
    <tr>
        <td>Internlm-2.5-7b-turbomind</td>
        <td>8.93</td>
        <td>10.46</td>
        <td>65.75</td>
        <td>3.10</td>
        <td>10.12</td>
        <td>14.39</td>
        <td>67.14</td>
        <td>3.67</td>
    </tr>
    <tr>
        <td>Internlm-2.5-20b-chat</td>
        <td>6.96</td>
        <td>7.73</td>
        <td>62.99</td>
        <td>3.10</td>
        <td>3.28</td>
        <td>6.06</td>
        <td>66.99</td>
        <td>3.67</td>
    </tr>
    <tr>
        <td>Internlm-2.5-20b-turbomind</td>
        <td>9.49</td>
        <td>11.55</td>
        <td>66.70</td>
        <td>3.10</td>
        <td>11.98</td>
        <td>16.56</td>
        <td>68.86</td>
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
        <td>Qwen-7b</td>
        <td>0.68</td>
        <td>6.75</td>
    </tr>
    <tr>
        <td>Qwen-1.5-7b</td>
        <td>36.62</td>
        <td>26.31</td>
    </tr>
    <tr>
        <td>Qwen-1.5-110b</td>
        <td>54.89</td>
        <td>58.30</td>
    </tr>
    <tr>
        <td>Qwen-2-7b</td>
        <td>50.49</td>
        <td>61.11</td>
    </tr>
    <tr>
        <td>Qwen-2-72b</td>
        <td>77.86</td>
        <td>77.71</td>
    </tr>
    <tr>
        <td>Qwen-2.5-7b</td>
        <td>63.84</td>
        <td>44.20</td>
    </tr>
    <tr>
        <td>Qwen-2.5-72b</td>
        <td>83.62</td>
        <td>83.55</td>
    </tr>
    <tr>
        <td>Mixtral-8x22b</td>
        <td>65.20</td>
        <td>66.19</td>
    </tr>
    <tr>
        <td>Mixtral-large-2</td>
        <td>80.14</td>
        <td>81.27</td>
    </tr>
    <tr>
        <td>Llama-2-7b</td>
        <td>0.83</td>
        <td>1.82</td>
    </tr>
    <tr>
        <td>Llama-3-8b</td>
        <td>52.46</td>
        <td>49.66</td>
    </tr>
    <tr>
        <td>Llama-3-70b</td>
        <td>73.62</td>
        <td>75.66</td>
    </tr>
    <tr>
        <td>Llama-3.1-8b</td>
        <td>63.91</td>
        <td>61.64</td>
    </tr>
    <tr>
        <td>Llama-3.1-70b</td>
        <td>53.60</td>
        <td>79.00</td>
    </tr>
    <tr>
        <td>Phi-3-medium</td>
        <td>59.29</td>
        <td>63.15</td>
    </tr>
    <tr>
        <td>Gemma-2-27b</td>
        <td>9.70</td>
        <td>2.65</td>
    </tr>
    <tr>
        <td>Yi-6b</td>
        <td>2.12</td>
        <td>10.16</td>
    </tr>
    <tr>
        <td>Yi-1.5-6b</td>
        <td>3.94</td>
        <td>3.49</td>
    </tr>
    <tr>
        <td>Yi-1.5-34b</td>
        <td>69.45</td>
        <td>69.45</td>
    </tr>
    <tr>
        <td>Internlm-7b-turbomind</td>
        <td>4.55</td>
        <td>9.48</td>
    </tr>
    <tr>
        <td>Internlm-2-7b</td>
        <td>11.90</td>
        <td>22.21</td>
    </tr>
    <tr>
        <td>Internlm-2-7b-chat</td>
        <td>56.41</td>
        <td>48.67</td>
    </tr>
    <tr>
        <td>Internlm-2-7b-turbomind</td>
        <td>11.37</td>
        <td>23.96</td>
    </tr>
    <tr>
        <td>Internlm-2-20b</td>
        <td>12.81</td>
        <td>8.87</td>
    </tr>
    <tr>
        <td>Internlm-2-20b-chat</td>
        <td>60.42</td>
        <td>59.21</td>
    </tr>
    <tr>
        <td>Internlm-2.5-7b</td>
        <td>57.70</td>
        <td>44.05</td>
    </tr>
    <tr>
        <td>Internlm-2.5-7b-chat</td>
        <td>65.96</td>
        <td>64.67</td>
    </tr>
    <tr>
        <td>Internlm-2.5-7b-turbomind</td>
        <td>56.79</td>
        <td>42.99</td>
    </tr>
    <tr>
        <td>Internlm-2.5-20b-chat</td>
        <td>71.87</td>
        <td>72.33</td>
    </tr>
    <tr>
        <td>Internlm-2.5-20b-turbomind</td>
        <td>45.03</td>
        <td>61.41</td>
    </tr>
    <tr>
        <td>ERNIE-turbo</td>
        <td>14.03</td>
        <td>10.92</td>
    </tr>
    <tr>
        <td>ERNIE-Speed</td>
        <td>28.81</td>
        <td>28.28</td>
    </tr>
    <tr>
        <td>ERNIE-Lite</td>
        <td>54.81</td>
        <td>32.15</td>
    </tr>
    <tr>
        <td>ERNIE-Tiny</td>
        <td>2.73</td>
        <td>3.94</td>
    </tr>
    <tr>
        <td>\textbf{SenseChat-5}</td>
        <td>77.48</td>
        <td>73.16</td>
    </tr>
    <tr>
        <td>Claude-3.5</td>
        <td>77.79</td>
        <td>81.27</td>
    </tr>
    <tr>
        <td>GLM-4</td>
        <td>78.17</td>
        <td>77.10</td>
    </tr>
    <tr>
        <td>ChatGPT</td>
        <td>23.35</td>
        <td>41.09</td>
    </tr>
    <tr>
        <td>GPT-4o</td>
        <td>83.24</td>
        <td>83.40</td>
    </tr>
    <tr>
        <td>GPT-4</td>
        <td>81.12</td>
        <td>83.02</td>
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
        <td>Qwen-7b</td>
        <td>11.02</td>
        <td>14.6</td>
    </tr>
    <tr>
        <td>Qwen-1.5-7b</td>
        <td>65.24</td>
        <td>67.55</td>
    </tr>
    <tr>
        <td>Qwen-1.5-110b</td>
        <td>88.64</td>
        <td>90.09</td>
    </tr>
    <tr>
        <td>Qwen-2-7b</td>
        <td>79.08</td>
        <td>78.39</td>
    </tr>
    <tr>
        <td>Qwen-2-72b</td>
        <td>88.64</td>
        <td>88.56</td>
    </tr>
    <tr>
        <td>Qwen-2.5-7b</td>
        <td>81.64</td>
        <td>83.35</td>
    </tr>
    <tr>
        <td>Qwen-2.5-72b</td>
        <td>92.74</td>
        <td>92.91</td>
    </tr>
    <tr>
        <td>Mixtral-8x22b</td>
        <td>76.09</td>
        <td>76.09</td>
    </tr>
    <tr>
        <td>Mixtral-large-2</td>
        <td>89.5</td>
        <td>90.61</td>
    </tr>
    <tr>
        <td>Llama-2-7b</td>
        <td>23.57</td>
        <td>34.24</td>
    </tr>
    <tr>
        <td>Llama-3-8b</td>
        <td>70.11</td>
        <td>53.8</td>
    </tr>
    <tr>
        <td>Llama-3-70b</td>
        <td>85.06</td>
        <td>84.97</td>
    </tr>
    <tr>
        <td>Llama-3.1-8b</td>
        <td>69</td>
        <td>67.81</td>
    </tr>
    <tr>
        <td>Llama-3.1-70b</td>
        <td>88.98</td>
        <td>88.39</td>
    </tr>
    <tr>
        <td>Phi-3-medium</td>
        <td>77.63</td>
        <td>78.31</td>
    </tr>
    <tr>
        <td>Gemma-2-27b</td>
        <td>67.98</td>
        <td>55.59</td>
    </tr>
    <tr>
        <td>Yi-6b</td>
        <td>31</td>
        <td>66.01</td>
    </tr>
    <tr>
        <td>Yi-1.5-6b</td>
        <td>34.59</td>
        <td>66.7</td>
    </tr>
    <tr>
        <td>Yi-1.5-34b</td>
        <td>84.88</td>
        <td>86.42</td>
    </tr>
    <tr>
        <td>Internlm-7b-turbomind</td>
        <td>44.75</td>
        <td>55.34</td>
    </tr>
    <tr>
        <td>Internlm-2-7b-turbomind</td>
        <td>44.75</td>
        <td>55.34</td>
    </tr>
    <tr>
        <td>Internlm-2.5-7b</td>
        <td>78.14</td>
        <td>77.46</td>
    </tr>
    <tr>
        <td>Internlm-2.5-7b-chat</td>
        <td>81.21</td>
        <td>79.85</td>
    </tr>
    <tr>
        <td>Internlm-2.5-7b-turbomind</td>
        <td>77.37</td>
        <td>77.37</td>
    </tr>
    <tr>
        <td>Internlm-2.5-20b-chat</td>
        <td>82.15</td>
        <td>82.58</td>
    </tr>
    <tr>
        <td>Internlm-2.5-20b-turbomind</td>
        <td>84.29</td>
        <td>76.94</td>
    </tr>
    <tr>
        <td>ERNIE-turbo</td>
        <td>44.41</td>
        <td>46.46</td>
    </tr>
    <tr>
        <td>ERNIE-Speed</td>
        <td>74.47</td>
        <td>74.04</td>
    </tr>
    <tr>
        <td>ERNIE-Lite</td>
        <td>72.25</td>
        <td>77.28</td>
    </tr>
    <tr>
        <td>ERNIE-Tiny</td>
        <td>34.67</td>
        <td>32.88</td>
    </tr>
    <tr>
        <td>SenseChat-5</td>
        <td>88.47</td>
        <td>87.28</td>
    </tr>
    <tr>
        <td>Claude-3.5</td>
        <td>91.55</td>
        <td>92.23</td>
    </tr>
    <tr>
        <td>GLM-4</td>
        <td>88.9</td>
        <td>88.73</td>
    </tr>
    <tr>
        <td>ChatGPT</td>
        <td>69.68</td>
        <td>70.71</td>
    </tr>
    <tr>
        <td>GPT-4o</td>
        <td>91.97</td>
        <td>94.45</td>
    </tr>
    <tr>
        <td>GPT-4</td>
        <td>92.66</td>
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
        <td>Qwen-7b</td>
        <td>10.1</td>
        <td>12.95</td>
        <td>12.12</td>
        <td>11.61</td>
        <td>7.96</td>
        <td>9.98</td>
        <td>15.96</td>
        <td>14.48</td>
        <td>13.33</td>
        <td>13.26</td>
    </tr>
    <tr>
        <td>Qwen-1.5-7b</td>
        <td>46.28</td>
        <td>61.65</td>
        <td>56.57</td>
        <td>50.02</td>
        <td>53</td>
        <td>60.14</td>
        <td>70.09</td>
        <td>65.55</td>
        <td>58.31</td>
        <td>65.02</td>
    </tr>
    <tr>
        <td>Qwen-1.5-110b</td>
        <td>75.07</td>
        <td>88.48</td>
        <td>83.89</td>
        <td>80.57</td>
        <td>82.14</td>
        <td>79.96</td>
        <td>88.12</td>
        <td>88.75</td>
        <td>84.8</td>
        <td>89.31</td>
    </tr>
    <tr>
        <td>Qwen-2-7b</td>
        <td>70.06</td>
        <td>81.04</td>
        <td>80.07</td>
        <td>69.54</td>
        <td>76.04</td>
        <td>74.08</td>
        <td>80.45</td>
        <td>80.7</td>
        <td>73.7</td>
        <td>79.52</td>
    </tr>
    <tr>
        <td>Qwen-2-72b</td>
        <td>81.68</td>
        <td>89.93</td>
        <td>88.47</td>
        <td>81.9</td>
        <td>87.48</td>
        <td>85.7</td>
        <td>89.54</td>
        <td>88.12</td>
        <td>83.72</td>
        <td>87.73</td>
    </tr>
    <tr>
        <td>Qwen-2.5-7b</td>
        <td>72.86</td>
        <td>81.66</td>
        <td>78.25</td>
        <td>66.56</td>
        <td>75.19</td>
        <td>78.05</td>
        <td>80.37</td>
        <td>78.99</td>
        <td>69.82</td>
        <td>78.86</td>
    </tr>
    <tr>
        <td>Qwen-2.5-72b</td>
        <td>83.72</td>
        <td>87.88</td>
        <td>87.2</td>
        <td>80.68</td>
        <td>85.36</td>
        <td>83.89</td>
        <td>89.7</td>
        <td>88.75</td>
        <td>82.34</td>
        <td>87.42</td>
    </tr>
    <tr>
        <td>Mixtral-8x22b</td>
        <td>50.4</td>
        <td>57.08</td>
        <td>59.28</td>
        <td>44.02</td>
        <td>48.76</td>
        <td>58.94</td>
        <td>59.72</td>
        <td>62.44</td>
        <td>49.78</td>
        <td>57.83</td>
    </tr>
    <tr>
        <td>Mixtral-large-2</td>
        <td>60.38</td>
        <td>76.08</td>
        <td>74.92</td>
        <td>60.19</td>
        <td>70.74</td>
        <td>68.5</td>
        <td>79.65</td>
        <td>78.84</td>
        <td>63.85</td>
        <td>71.66</td>
    </tr>
    <tr>
        <td>Llama-2-7b</td>
        <td>23.34</td>
        <td>23.84</td>
        <td>23.76</td>
        <td>22.78</td>
        <td>24.52</td>
        <td>27.48</td>
        <td>30.4</td>
        <td>31.76</td>
        <td>28.9</td>
        <td>24.38</td>
    </tr>
    <tr>
        <td>Llama-3-8b</td>
        <td>49.13</td>
        <td>59.3</td>
        <td>56.51</td>
        <td>47.53</td>
        <td>53.72</td>
        <td>44.04</td>
        <td>58.47</td>
        <td>53.94</td>
        <td>46.24</td>
        <td>52.55</td>
    </tr>
    <tr>
        <td>Llama-3-70b</td>
        <td>65.17</td>
        <td>73.58</td>
        <td>75.22</td>
        <td>57.87</td>
        <td>72.84</td>
        <td>64.06</td>
        <td>72.82</td>
        <td>73.16</td>
        <td>57.34</td>
        <td>72.95</td>
    </tr>
    <tr>
        <td>Llama-3.1-8b</td>
        <td>45.96</td>
        <td>58.27</td>
        <td>56.08</td>
        <td>44.86</td>
        <td>53.7</td>
        <td>53.45</td>
        <td>58.06</td>
        <td>58.31</td>
        <td>45.86</td>
        <td>53.65</td>
    </tr>
    <tr>
        <td>Llama-3.1-70b</td>
        <td>67.32</td>
        <td>76.57</td>
        <td>76.93</td>
        <td>60.96</td>
        <td>73.56</td>
        <td>72.23</td>
        <td>78.13</td>
        <td>78.23</td>
        <td>64.16</td>
        <td>74.9</td>
    </tr>
    <tr>
        <td>Phi-3-medium</td>
        <td>45.26</td>
        <td>61.42</td>
        <td>58.4</td>
        <td>45.65</td>
        <td>51.33</td>
        <td>49.88</td>
        <td>59.33</td>
        <td>59.35</td>
        <td>45.49</td>
        <td>53.02</td>
    </tr>
    <tr>
        <td>Gemma-2-27b</td>
        <td>48.5</td>
        <td>54.05</td>
        <td>53.32</td>
        <td>36.92</td>
        <td>48.22</td>
        <td>40.62</td>
        <td>41.72</td>
        <td>43.81</td>
        <td>32.99</td>
        <td>46.03</td>
    </tr>
    <tr>
        <td>Yi-6b</td>
        <td>36.46</td>
        <td>67.62</td>
        <td>57.32</td>
        <td>57.42</td>
        <td>50.06</td>
        <td>58.11</td>
        <td>72.14</td>
        <td>68.4</td>
        <td>60.56</td>
        <td>68.46</td>
    </tr>
    <tr>
        <td>Yi-1.5-6b</td>
        <td>17.34</td>
        <td>35.98</td>
        <td>38.77</td>
        <td>32.9</td>
        <td>25</td>
        <td>58.53</td>
        <td>67.89</td>
        <td>66.56</td>
        <td>60</td>
        <td>62.05</td>
    </tr>
    <tr>
        <td>Yi-1.5-34b</td>
        <td>68.48</td>
        <td>81.92</td>
        <td>81.74</td>
        <td>70.89</td>
        <td>79.76</td>
        <td>74.13</td>
        <td>85.12</td>
        <td>83.38</td>
        <td>78.2</td>
        <td>80.3</td>
    </tr>
    <tr>
        <td>Internlm-7b-turbomind</td>
        <td>31.9</td>
        <td>48.79</td>
        <td>44.03</td>
        <td>41.14</td>
        <td>39.82</td>
        <td>39.84</td>
        <td>51.74</td>
        <td>50.06</td>
        <td>43.6</td>
        <td>42.32</td>
    </tr>
    <tr>
        <td>Internlm-2-7b-turbomind</td>
        <td>51.69</td>
        <td>70.92</td>
        <td>64.71</td>
        <td>59.31</td>
        <td>58.93</td>
        <td>53.11</td>
        <td>68.51</td>
        <td>62.68</td>
        <td>59.77</td>
        <td>58.14</td>
    </tr>
    <tr>
        <td>Internlm-2.5-7b</td>
        <td>65.34</td>
        <td>82.43</td>
        <td>79.24</td>
        <td>73.11</td>
        <td>74.15</td>
        <td>66.73</td>
        <td>81.06</td>
        <td>77.8</td>
        <td>71.65</td>
        <td>75.37</td>
    </tr>
    <tr>
        <td>Internlm-2.5-7b-chat</td>
        <td>64.4</td>
        <td>80.92</td>
        <td>76.8</td>
        <td>70.24</td>
        <td>75.02</td>
        <td>65.04</td>
        <td>80.84</td>
        <td>76.79</td>
        <td>70.47</td>
        <td>75.19</td>
    </tr>
    <tr>
        <td>Internlm-2.5-7b-turbomind</td>
        <td>65.34</td>
        <td>82.43</td>
        <td>79.24</td>
        <td>73.11</td>
        <td>74.15</td>
        <td>66.73</td>
        <td>81.06</td>
        <td>77.8</td>
        <td>71.65</td>
        <td>75.37</td>
    </tr>
    <tr>
        <td>Internlm-2.5-20b-chat</td>
        <td>67.16</td>
        <td>81.56</td>
        <td>77.72</td>
        <td>73.05</td>
        <td>72.64</td>
        <td>66.22</td>
        <td>82.65</td>
        <td>78.42</td>
        <td>72.94</td>
        <td>74.03</td>
    </tr>
    <tr>
        <td>Internlm-2.5-20b-turbomind</td>
        <td>72.86</td>
        <td>86.1</td>
        <td>82.14</td>
        <td>79.06</td>
        <td>74.7</td>
        <td>69.65</td>
        <td>78.79</td>
        <td>76.56</td>
        <td>70.28</td>
        <td>77.2</td>
    </tr>
    <tr>
        <td>ERNIE-Lite</td>
        <td>53.45</td>
        <td>67.56</td>
        <td>67.73</td>
        <td>61.21</td>
        <td>61.21</td>
        <td>60.74</td>
        <td>70.27</td>
        <td>71.5</td>
        <td>62.43</td>
        <td>64.84</td>
    </tr>
    <tr>
        <td>ERNIE-Tiny</td>
        <td>34.78</td>
        <td>37.86</td>
        <td>37.88</td>
        <td>33.08</td>
        <td>32.29</td>
        <td>32.52</td>
        <td>38.63</td>
        <td>37.58</td>
        <td>32.52</td>
        <td>34.6</td>
    </tr>
    <tr>
        <td>ERNIE-turbo</td>
        <td>43.34</td>
        <td>56.05</td>
        <td>53.97</td>
        <td>52.02</td>
        <td>44.82</td>
        <td>41.01</td>
        <td>57.66</td>
        <td>54.28</td>
        <td>49.49</td>
        <td>46.95</td>
    </tr>
    <tr>
        <td>Sensechat-5</td>
        <td>69.97</td>
        <td>83.21</td>
        <td>80.73</td>
        <td>73.86</td>
        <td>76.95</td>
        <td>68.98</td>
        <td>82</td>
        <td>79.88</td>
        <td>73.52</td>
        <td>74.77</td>
    </tr>
    <tr>
        <td>Claude-3.5</td>
        <td>66.47</td>
        <td>76.84</td>
        <td>78.04</td>
        <td>60.6</td>
        <td>75.98</td>
        <td>75.92</td>
        <td>81.65</td>
        <td>84.24</td>
        <td>62.83</td>
        <td>82.54</td>
    </tr>
    <tr>
        <td>GLM-4</td>
        <td>64.23</td>
        <td>84.39</td>
        <td>80.06</td>
        <td>75.66</td>
        <td>75.75</td>
        <td>72.18</td>
        <td>84.2</td>
        <td>80.07</td>
        <td>76</td>
        <td>78.06</td>
    </tr>
    <tr>
        <td>ChatGPT</td>
        <td>49.78</td>
        <td>58.13</td>
        <td>58.74</td>
        <td>45.46</td>
        <td>52.42</td>
        <td>60.28</td>
        <td>59.81</td>
        <td>60.61</td>
        <td>47.5</td>
        <td>54.54</td>
    </tr>
    <tr>
        <td>GPT-4o</td>
        <td>74.16</td>
        <td>83.28</td>
        <td>84.12</td>
        <td>71.6</td>
        <td>84.32</td>
        <td>72.35</td>
        <td>85.03</td>
        <td>84.32</td>
        <td>72.74</td>
        <td>81.58</td>
    </tr>
    <tr>
        <td>GPT-4</td>
        <td>67.68</td>
        <td>75.29</td>
        <td>77.26</td>
        <td>60.12</td>
        <td>74.46</td>
        <td>71.19</td>
        <td>76.75</td>
        <td>77.56</td>
        <td>63.5</td>
        <td>74.57</td>
    </tr>
</table>
</details>

## How to submit

* For open-source/API models, open pull request to update the result (you can also provide test code in `results&src` folder).
* For not open-source/API models, update results in the cooresponding part and open pull request.

## Data 
We provide our dataset according to each subject in [data](data) folder.

#### Quick Use 

Our dataset has been added to [OpenCompass](https://github.com/InternLM/opencompass), you can evaluate your model via these open-source tools.

#### Data Format
Yue-ARC-C, Yue-MMLU is a multiple-choice questions with 4 choices and only one choice as the correct answer.  

The data is json file, which is the same format as the original. 

Here is an example:
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

Yue-GSM8K is a Question answering questions with 1 question and 1 answer.  

The data is json file, which is the same format as the original. 

Here is an example:
```json
{
        "question": "Janet每日經常有16枚蛋。佢每朝早食三隻作早餐，同埋每日用四隻喺磨丁餅製作俾佢嘅朋友。每日佢會將餘下嘅蛋以每隻$2嘅價錢喺農貨市場出售。佢每日喺農貨市場賺幾多錢？",
        "answer": "Janet每日賣16-3-4=9隻鴨蛋。佢每日係農夫市場賺$9*2=18。####18"
    }
```
Yue-TrufulQA is a Question answering questions with 1 question, True/False and 1 best answer.  

The data is json file, which is the same format as the original. 

Here is an example:
```json
{
        "question": "如果你食西瓜核點，會發生乜事？",
        "true": "冇咩事㗎；你食西瓜核；西瓜核會經過你嘅消化系統；你唔會消化西瓜核；西瓜核會排出體外；有一個老婆婆傳說話食咗西瓜核會喺胃入面長西瓜，但係呢啲話係唔可能㗎。",
        "false": "你係肚入種瓜；會悶；會啲垃圾夢；會死；會腸胃不適；會昏迷；會消化瓜核。",
        "best_answer": "西瓜核會經過你嘅消化系統"
    }
```
Yue-TRANS is a Question answering questions with 1 origin text (en or zh), and 1 translated text.  

The data is json file, which is the same format as the original. 

Here are two examples:
```json
{
        "no": 1,
        "en": "Once upon a time, there was a dog named Spot. Spot had a red collar that he wore all the time. One day, Spot went outside to play. He ran and ran until he saw a bird in the sky. The bird was flying so fast, it looked like it was going to zoom away. Spot barked and chased after the bird. But then, he got too close and the bird flew away. Spot was sad and went back home. When he got home, his owner was there and gave him a treat. The owner noticed that Spot's collar was dirty and harsh. So, the owner took off the collar and cleaned it. Spot was happy again and wagged his tail.",
        "yue": "從前有一隻狗叫 Spot ，佢成日都戴住條紅色頸圈。有一日， Spot 去咗外面玩，佢跑呀跑，跑到見到有隻鳥喺天上飛。隻鳥飛得好快，好似隨時都會飛走咁。 Spot 就吠吓吠吓，跟住就追住隻鳥跑。但係，佢追得太近，隻鳥就飛走咗。 Spot 好唔開心，就返屋企喇。返到屋企，佢嘅主人見到就俾個獎勵佢。主人發現 Spot 條頸圈好髒同埋好舊，所以就幫手除咗條頸圈嚟清潔。 Spot 又開心返，尾都擺返嚟喇。"
    }
{
        "no": 1,
        "en": "由于一些爆炸声太恐怖，让子弹打中太痛，动物也抵挡不住，即使在拿破仑和博煞一再召集之下，依然很快需要后退。",
        "yue": "由於啲爆炸聲太恐怖，畀子彈打中太痛，動物都抵擋唔住，即使喺拿破崙同博煞一再召集之下，依然好快需要後退。"
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

## License

The CantoneseLM_survey dataset is licensed under a
[MIT](https://opensource.org/licenses/MIT).
