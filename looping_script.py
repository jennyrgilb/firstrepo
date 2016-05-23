#script to create a .sh file to run multiple flirts and fslmaths
#the .sh can then be launched on a network or run locally
#becareful if running locally this script has the potenial to get really long
#no check function yet!!!!!!
#has capabilities to run flirt within script with nipy, currently OFF, uncomment to turn on
#GSHEARRER 05/18/2016

import os
import glob
#import nipype.interfaces.fsl as fsl

####check cost function you want to use####
#flt = fsl.FLIRT(bins=640, ###cost_func='mutualinfo'####, apply_xfm=TRUE, useqform=TRUE)
#fslmaths=fsl.maths(args='-thr 0.5','-bin')

#set paths
basepath='/Volumes/macX/juice/'#this should be the path to whatever directory your experiment lives in 
maskdir='/Volumes/macX/timecourse/'#this is the path to where ever you keep your masks
outputdir='/Volumes/macX/juice/w1subjects/masks/'
#open file to append to 
f=open('flirt_script.sh','a')


#flirt -in /Volumes/macX/timecourses/mask_roi002.nii -ref /Volumes/macX/juice/w1subjects/js02/juice1/swuabf.nii -applyxfm -usesqform -out mask002
#fslmaths mask002 -thr 0.5 -bin highres_mask002

#change directories
os.chdir(os.path.join(basepath,'w1subjects'))
#start loop
for ref_file in glob.glob('js*/juice*/swuabf.nii'):#look in every subject in every run for the swuab file
  print(ref_file)
  #flt.inputs.reference=os.path.join(basepath, ref_file)
  for mask in glob.glob(maskdir+'mask_roi*.nii'):#for each run, begin this loop
    #flt.inputs.in_file=mask
    number=input.split('/')[3]#this might need to be tweeked
    number2=number.strip('mask_roi')
    number_final=number2.strip('.nii')#this is the number you want for the output
    outputname='trans_mask_'+number_final#output name
    outpath=os.path.join(maskdir, outputname)#output path
    binname='highres_mask_'+number_final#bin name for fslmaths
    binpath=os.path.join(maskdir, binname)#path to binmask for fslmaths
    #flt.inputs.out_file=os.path.join(outputdir,finaloutput)
    #binary_output=os.path.join(outputdir,binoutput)
    ####START FSL SCRIPT HERE######
    #flt.inputs.output_type = "NIFTI_GZ"
    #log=flt.cmdline
    #res = flt.run()
    ####### this is taking the variables and writing them to the file######
    flirt_cmd='flirt -in '+outpath+' -ref '+ref_file+' -applyxfm -usesqform -out '+finaloutput
    fslmath_cmd='fslmaths '+finaloutput+' -thr 0.5 -bin '+binary_output
    f.write('%s\n' % (flirt_cmd,))
    f.write('%s\n' % (fslmath_cmd))
#close the open file
f.close()
