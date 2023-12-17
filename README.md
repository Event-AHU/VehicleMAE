
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

<p align="center">
  <img width="80%" src="https://github.com/Event-AHU/VehicleMAE/blob/main/figures/reconst_vis.jpg" alt="reconst_vis"/>
</p> 

<p align="center">
  <img width="80%" src="https://github.com/Event-AHU/VehicleMAE/blob/main/figures/attentionmaps.jpg" alt="attentionmaps"/>
</p> 

<table class="MsoTableGrid" border="1" cellspacing="0" cellpadding="0" width="590" style="width:442.6pt;border-collapse:collapse;border:none">
 <tbody><tr style="height:15.9pt">
  <td width="94" rowspan="2" valign="top" style="width:70.65pt;border:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Method</span></p>
  </td>
  <td width="86" rowspan="2" valign="top" style="width:64.7pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Dataset</span></p>
  </td>
  <td width="153" colspan="3" valign="top" style="width:114.6pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">VAR</span></p>
  </td>
  <td width="102" colspan="2" valign="top" style="width:76.7pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">V-Reid</span></p>
  </td>
  <td width="51" valign="top" style="width:38.5pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal"><span lang="EN-US">VFR</span></p>
  </td>
  <td width="103" colspan="2" valign="top" style="width:77.45pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">VPS</span></p>
  </td>
 </tr>
 <tr style="height:16.3pt">
  <td width="51" valign="top" style="width:38.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal"><span lang="EN-US">mA</span></p>
  </td>
  <td width="51" valign="top" style="width:38.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal"><span lang="EN-US">Acc</span></p>
  </td>
  <td width="51" valign="top" style="width:38.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal"><span lang="EN-US">F1</span></p>
  </td>
  <td width="51" valign="top" style="width:38.55pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">mAP</span></p>
  </td>
  <td width="51" valign="top" style="width:38.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">R1</span></p>
  </td>
  <td width="51" valign="top" style="width:38.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">ACC</span></p>
  </td>
  <td width="52" valign="top" style="width:38.65pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">mIou</span></p>
  </td>
  <td width="52" valign="top" style="width:38.8pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">mAcc</span></p>
  </td>
 </tr>
 <tr style="height:16.3pt">
  <td width="94" valign="top" style="width:70.65pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Scratch</span></p>
  </td>
  <td width="86" valign="top" style="width:64.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">-</span></p>
  </td>
  <td width="51" valign="top" style="width:38.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">84.67</span></p>
  </td>
  <td width="51" valign="top" style="width:38.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">80.86</span></p>
  </td>
  <td width="51" valign="top" style="width:38.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">84.90</span></p>
  </td>
  <td width="51" valign="top" style="width:38.55pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">35.3</span></p>
  </td>
  <td width="51" valign="top" style="width:38.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">57.3</span></p>
  </td>
  <td width="51" valign="top" style="width:38.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">24.8</span></p>
  </td>
  <td width="52" valign="top" style="width:38.65pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">49.36</span></p>
  </td>
  <td width="52" valign="top" style="width:38.8pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">59.22</span></p>
  </td>
 </tr>
 <tr style="height:15.9pt">
  <td width="94" valign="top" style="width:70.65pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">MoCov3</span></p>
  </td>
  <td width="86" valign="top" style="width:64.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Imagenet-1K</span></p>
  </td>
  <td width="51" valign="top" style="width:38.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">90.38</span></p>
  </td>
  <td width="51" valign="top" style="width:38.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">93.88</span></p>
  </td>
  <td width="51" valign="top" style="width:38.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">95.33</span></p>
  </td>
  <td width="51" valign="top" style="width:38.55pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">75.5</span></p>
  </td>
  <td width="51" valign="top" style="width:38.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">94.4</span></p>
  </td>
  <td width="51" valign="top" style="width:38.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">91.3</span></p>
  </td>
  <td width="52" valign="top" style="width:38.65pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">73.17</span></p>
  </td>
  <td width="52" valign="top" style="width:38.8pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">78.60</span></p>
  </td>
 </tr>
 <tr style="height:15.9pt">
  <td width="94" valign="top" style="width:70.65pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">DINO</span></p>
  </td>
  <td width="86" valign="top" style="width:64.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Imagenet-1K</span></p>
  </td>
  <td width="51" valign="top" style="width:38.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">89.92</span></p>
  </td>
  <td width="51" valign="top" style="width:38.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">91.09</span></p>
  </td>
  <td width="51" valign="top" style="width:38.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">93.11</span></p>
  </td>
  <td width="51" valign="top" style="width:38.55pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">64.3</span></p>
  </td>
  <td width="51" valign="top" style="width:38.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">91.5</span></p>
  </td>
  <td width="51" valign="top" style="width:38.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">-</span></p>
  </td>
  <td width="52" valign="top" style="width:38.65pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">68.43</span></p>
  </td>
  <td width="52" valign="top" style="width:38.8pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">73.37</span></p>
  </td>
 </tr>
 <tr style="height:15.9pt">
  <td width="94" valign="top" style="width:70.65pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">IBOT</span></p>
  </td>
  <td width="86" valign="top" style="width:64.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Imagenet-1K</span></p>
  </td>
  <td width="51" valign="top" style="width:38.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">89.51</span></p>
  </td>
  <td width="51" valign="top" style="width:38.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">90.17</span></p>
  </td>
  <td width="51" valign="top" style="width:38.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">92.37</span></p>
  </td>
  <td width="51" valign="top" style="width:38.55pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">68.9</span></p>
  </td>
  <td width="51" valign="top" style="width:38.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">92.6</span></p>
  </td>
  <td width="51" valign="top" style="width:38.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">81.1</span></p>
  </td>
  <td width="52" valign="top" style="width:38.65pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">66.03</span></p>
  </td>
  <td width="52" valign="top" style="width:38.8pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">71.06</span></p>
  </td>
 </tr>
 <tr style="height:16.3pt">
  <td width="94" valign="top" style="width:70.65pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">MAE</span></p>
  </td>
  <td width="86" valign="top" style="width:64.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Imagenet-1K</span></p>
  </td>
  <td width="51" valign="top" style="width:38.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">89.69</span></p>
  </td>
  <td width="51" valign="top" style="width:38.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">93.60</span></p>
  </td>
  <td width="51" valign="top" style="width:38.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">95.08</span></p>
  </td>
  <td width="51" valign="top" style="width:38.55pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">76.7</span></p>
  </td>
  <td width="51" valign="top" style="width:38.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">95.8</span></p>
  </td>
  <td width="51" valign="top" style="width:38.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">91.2</span></p>
  </td>
  <td width="52" valign="top" style="width:38.65pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">69.54</span></p>
  </td>
  <td width="52" valign="top" style="width:38.8pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.3pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">75.36</span></p>
  </td>
 </tr>
 <tr style="height:15.9pt">
  <td width="94" valign="top" style="width:70.65pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">MAE</span></p>
  </td>
  <td width="86" valign="top" style="width:64.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Autobot1M</span></p>
  </td>
  <td width="51" valign="top" style="width:38.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">90.19</span></p>
  </td>
  <td width="51" valign="top" style="width:38.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">94.06</span></p>
  </td>
  <td width="51" valign="top" style="width:38.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">95.43</span></p>
  </td>
  <td width="51" valign="top" style="width:38.55pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">75.5</span></p>
  </td>
  <td width="51" valign="top" style="width:38.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">95.4</span></p>
  </td>
  <td width="51" valign="top" style="width:38.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">91.3</span></p>
  </td>
  <td width="52" valign="top" style="width:38.65pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">69.00</span></p>
  </td>
  <td width="52" valign="top" style="width:38.8pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">75.36</span></p>
  </td>
 </tr>
 <tr style="height:15.9pt">
  <td width="94" valign="top" style="width:70.65pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">VehicleMAE</span></p>
  </td>
  <td width="86" valign="top" style="width:64.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Autobot1M</span></p>
  </td>
  <td width="51" valign="top" style="width:38.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">92.21</span></p>
  </td>
  <td width="51" valign="top" style="width:38.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">94.91</span></p>
  </td>
  <td width="51" valign="top" style="width:38.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">96.17</span></p>
  </td>
  <td width="51" valign="top" style="width:38.55pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">85.6</span></p>
  </td>
  <td width="51" valign="top" style="width:38.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">97.9</span></p>
  </td>
  <td width="51" valign="top" style="width:38.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">94.5</span></p>
  </td>
  <td width="52" valign="top" style="width:38.65pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">73.29</span></p>
  </td>
  <td width="52" valign="top" style="width:38.8pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.9pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">80.22</span></p>
  </td>
 </tr>
</tbody></table>

## Acknowledgement 


## Citation 
```bibtex

```


if you have any problems with this work, please leave an issue. 
