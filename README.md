
<p align="center">
  <img width="50%" src="https://github.com/Event-AHU/VehicleMAE/blob/main/figures/logo.jpg" alt="firstIMG"/>
</p> 



Official PyTorch implementation of **Structural Information Guided Multimodal Pre-training for Vehicle-centric Perception**, Xiao Wang, Wentao Wu, Chenglong Li, Zhicheng Zhao, Zhe Chen, Yukai Shi, Jin Tang, AAAI-2024 
[[Paper]()] 



## Abstract 

<p align="center">
  <img width="100%" src="https://github.com/Event-AHU/VehicleMAE/blob/main/figures/firstIMG.jpg" alt="firstIMG"/>
</p> 



## Our Proposed Framework VehicleMAE  

<p align="center">
  <img width="100%" src="https://github.com/Event-AHU/VehicleMAE/blob/main/figures/framework.jpg" alt="framework"/>
</p> 

## Environment Setting 


## Dataset Download 


<p align="center">
  <img width="100%" src="https://github.com/Event-AHU/VehicleMAE/blob/main/figures/data_show.jpg" alt="data_show"/>
</p> 

## Pre-trained Model Download
 Pre-trained Model  | Vit-base 
 ---- | -----  
 Pre-trained checkpoint  | [download](https://pan.baidu.com/s/1wB2QdzItdVVYQQ491ZOOrA?pwd=6zkx)
 Extracted code |6zkx


## Training and Testing 


## Experimental Results 

<table class="MsoTableGrid" border="1" cellspacing="0" cellpadding="0" width="620" style="width: 620px;border-collapse:collapse;border:none;height: 200px;">
 <tbody><tr style="height:15.6pt">
  <td width="95" rowspan="2" valign="top" style="width:71.05pt;border:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="margin-top:12.0pt;text-align:center"><b><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">Method</span></b></p>
  </td>
  <td width="94" rowspan="2" valign="top" style="width:90.15pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="margin-top:12.0pt;text-align:center"><b><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">Dataset</span></b></p>
  </td>
  <td width="154" colspan="3" valign="top" style="width:115.65pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">VAR</span></b></p>
  </td>
  <td width="89" colspan="2" valign="top" style="width:66.8pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">V-Reid</span></b></p>
  </td>
  <td width="45" valign="top" style="width:34.0pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">VFR</span></b></p>
  </td>
  <td width="100" colspan="2" valign="top" style="width:75.15pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">VPS</span></b></p>
  </td>
 </tr>
 <tr style="height:15.95pt">
  <td width="57" valign="top" style="width:42.55pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">mA</span></p>
  </td>
  <td width="49" valign="top" style="width:36.65pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">Acc</span></p>
  </td>
  <td width="49" valign="top" style="width:36.4pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">F1</span></p>
  </td>
  <td width="45" valign="top" style="width:34.0pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">mAP</span></p>
  </td>
  <td width="44" valign="top" style="width:32.75pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">R1</span></p>
  </td>
  <td width="45" valign="top" style="width:34.0pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">Acc</span></p>
  </td>
  <td width="50" valign="top" style="width:37.4pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">mIou</span></p>
  </td>
  <td width="50" valign="top" style="width:37.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">mAcc</span></p>
  </td>
 </tr>
 <tr style="height:15.95pt">
  <td width="95" valign="top" style="width:71.05pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">Scratch</span></b></p>
  </td>
  <td width="94" valign="top" style="width:90.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">-</span></p>
  </td>
  <td width="57" valign="top" style="width:42.55pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">84.67</span></p>
  </td>
  <td width="49" valign="top" style="width:36.65pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">80.86</span></p>
  </td>
  <td width="49" valign="top" style="width:36.4pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">84.90</span></p>
  </td>
  <td width="45" valign="top" style="width:34.0pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">35.3</span></p>
  </td>
  <td width="44" valign="top" style="width:32.75pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">57.3</span></p>
  </td>
  <td width="45" valign="top" style="width:34.0pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">24.8</span></p>
  </td>
  <td width="50" valign="top" style="width:37.4pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">49.36</span></p>
  </td>
  <td width="50" valign="top" style="width:37.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">59.22</span></p>
  </td>
 </tr>
 <tr style="height:15.6pt">
  <td width="95" valign="top" style="width:71.05pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">MoCov3</span></b></p>
  </td>
  <td width="94" valign="top" style="width:90.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">Imagenet-1K</span></p>
  </td>
  <td width="57" valign="top" style="width:42.55pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">90.38</span></p>
  </td>
  <td width="49" valign="top" style="width:36.65pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">93.88</span></p>
  </td>
  <td width="49" valign="top" style="width:36.4pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">95.33</span></p>
  </td>
  <td width="45" valign="top" style="width:34.0pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">75.5</span></p>
  </td>
  <td width="44" valign="top" style="width:32.75pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">94.4</span></p>
  </td>
  <td width="45" valign="top" style="width:34.0pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">91.3</span></p>
  </td>
  <td width="50" valign="top" style="width:37.4pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">73.17</span></p>
  </td>
  <td width="50" valign="top" style="width:37.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">78.60</span></p>
  </td>
 </tr>
 <tr style="height:15.6pt">
  <td width="95" valign="top" style="width:71.05pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">DINO</span></b></p>
  </td>
  <td width="94" valign="top" style="width:90.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">Imagenet-1K</span></p>
  </td>
  <td width="57" valign="top" style="width:42.55pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">89.92</span></p>
  </td>
  <td width="49" valign="top" style="width:36.65pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">91.09</span></p>
  </td>
  <td width="49" valign="top" style="width:36.4pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">93.11</span></p>
  </td>
  <td width="45" valign="top" style="width:34.0pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">64.3</span></p>
  </td>
  <td width="44" valign="top" style="width:32.75pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">91.5</span></p>
  </td>
  <td width="45" valign="top" style="width:34.0pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">-</span></p>
  </td>
  <td width="50" valign="top" style="width:37.4pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">68.43</span></p>
  </td>
  <td width="50" valign="top" style="width:37.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">73.37</span></p>
  </td>
 </tr>
 <tr style="height:15.6pt">
  <td width="95" valign="top" style="width:71.05pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">IBOT</span></b></p>
  </td>
  <td width="94" valign="top" style="width:90.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">Imagenet-1K</span></p>
  </td>
  <td width="57" valign="top" style="width:42.55pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">89.51</span></p>
  </td>
  <td width="49" valign="top" style="width:36.65pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">90.17</span></p>
  </td>
  <td width="49" valign="top" style="width:36.4pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">92.37</span></p>
  </td>
  <td width="45" valign="top" style="width:34.0pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">68.9</span></p>
  </td>
  <td width="44" valign="top" style="width:32.75pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">92.6</span></p>
  </td>
  <td width="45" valign="top" style="width:34.0pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">81.1</span></p>
  </td>
  <td width="50" valign="top" style="width:37.4pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">66.03</span></p>
  </td>
  <td width="50" valign="top" style="width:37.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">71.06</span></p>
  </td>
 </tr>
 <tr style="height:15.95pt">
  <td width="95" valign="top" style="width:71.05pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">MAE</span></b></p>
  </td>
  <td width="94" valign="top" style="width:90.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">Imagenet-1K</span></p>
  </td>
  <td width="57" valign="top" style="width:42.55pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">89.69</span></p>
  </td>
  <td width="49" valign="top" style="width:36.65pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">93.60</span></p>
  </td>
  <td width="49" valign="top" style="width:36.4pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">95.08</span></p>
  </td>
  <td width="45" valign="top" style="width:34.0pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">76.7</span></p>
  </td>
  <td width="44" valign="top" style="width:32.75pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">95.8</span></p>
  </td>
  <td width="45" valign="top" style="width:34.0pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">91.2</span></p>
  </td>
  <td width="50" valign="top" style="width:37.4pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">69.54</span></p>
  </td>
  <td width="50" valign="top" style="width:37.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.95pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">75.36</span></p>
  </td>
 </tr>
 <tr style="height:15.6pt">
  <td width="95" valign="top" style="width:71.05pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">MAE</span></b></p>
  </td>
  <td width="94" valign="top" style="width:90.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">Autobot1M</span></p>
  </td>
  <td width="57" valign="top" style="width:42.55pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">90.19</span></p>
  </td>
  <td width="49" valign="top" style="width:36.65pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">94.06</span></p>
  </td>
  <td width="49" valign="top" style="width:36.4pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">95.43</span></p>
  </td>
  <td width="45" valign="top" style="width:34.0pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">75.5</span></p>
  </td>
  <td width="44" valign="top" style="width:32.75pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">95.4</span></p>
  </td>
  <td width="45" valign="top" style="width:34.0pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">91.3</span></p>
  </td>
  <td width="50" valign="top" style="width:37.4pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">69.00</span></p>
  </td>
  <td width="50" valign="top" style="width:37.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">75.36</span></p>
  </td>
 </tr>
 <tr style="height:15.6pt">
  <td width="95" valign="top" style="width:71.05pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">VehicleMAE</span></b></p>
  </td>
  <td width="94" valign="top" style="width:90.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">Autobot1M</span></p>
  </td>
  <td width="57" valign="top" style="width:42.55pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">92.21</span></p>
  </td>
  <td width="49" valign="top" style="width:36.65pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">94.91</span></p>
  </td>
  <td width="49" valign="top" style="width:36.4pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">96.17</span></p>
  </td>
  <td width="45" valign="top" style="width:34.0pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">85.6</span></p>
  </td>
  <td width="44" valign="top" style="width:32.75pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">97.9</span></p>
  </td>
  <td width="45" valign="top" style="width:34.0pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">94.5</span></p>
  </td>
  <td width="50" valign="top" style="width:37.4pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">73.29</span></p>
  </td>
  <td width="50" valign="top" style="width:37.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.6pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Times New Roman&quot;,serif">80.22</span></p>
  </td>
 </tr>
</tbody></table>

## Visual Results 

<p align="center">
  <img width="80%" src="https://github.com/Event-AHU/VehicleMAE/blob/main/figures/reconst_vis.jpg" alt="reconst_vis"/>
</p> 

<p align="center">
  <img width="80%" src="https://github.com/Event-AHU/VehicleMAE/blob/main/figures/attentionmaps.jpg" alt="attentionmaps"/>
</p> 

## Acknowledgement 


## Citation 
```bibtex

```


if you have any problems with this work, please leave an issue. 
