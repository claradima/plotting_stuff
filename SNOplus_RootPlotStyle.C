// Template macro for C/C++ with the SNO+ plot style
// Written by Ana Sofia Inacio (ana.carpinteiroinacio@physics.ox.ac.uk); contact me or Clara Dima for comments/suggestions
//
// General rules:
// - Every figure that shows SNO+ data needs to be marked (embedded on the figure) with “SNO+ Preliminary”
// - Data should be black points with error bars (where a single data series is shown)
// - MC should be a blue histogram (where a single model is shown)
// - Any fit function (not based on MC) should be red (when a single fit is shown)
// - Consistency in labelling: normalized R3 axes should be labelled "R^3 / R_AV^3"
// - Isotropy should be #beta_14 (i.e. the greek symbol, not the word)
// - No box around legend
// - For publication purposes, the favoured font type has been Times (New) Roman
//
// For plots that compare multiple data series (e.g. optics at different wavelengths) or multiple models or fits, 
// appropriately different colours, markers, line styles should be used to differentiate and clearly labelled in the legend.
// Check https://www.cta-observatory.org/wp-content/uploads/2020/10/CTA_ColourBlindness_BestPractices-1.pdf 
// for colorblind friendly color palletes and other guidelines
//
// When saving the figures, always choose to save in PDF format as it is a scalable vector graphic and can be scaled 
// infinitely without losing quality.
//
// Specific analyses may produce plots which require styles different than the ones exemplified here. Trying as much
// as possible to follow the style rules where possible will certainly make the approval process easier.
//
// To test the style, compile this code with root using:
// .L SNOplus_RootPublicationStyle.C
// and run with:
// SNOplus_RootPublicationStyle()

// Required to make the style work
#include "TROOT.h" 
#include "TStyle.h"
#include "TText.h"
#include "TLegend.h"
#include "TCanvas.h"

// Will depend on what you are plotting: just a fit/function (TF), histogram (TH), graph, etc
#include "TF1.h"
#include "TH1.h"
#include "TF2.h"
#include "TH2.h"
#include "TGraph.h"
#include "TGraphErrors.h"

void SNOplus_RootPlotStyle(){

  ////               ////
  //// Style Options ////
  ////               ////

  TStyle *snoStyle= new TStyle("snoplus","SNO+ plots style for publications");

  // Use plain black on white colors
  snoStyle->SetFrameBorderMode(0);
  snoStyle->SetCanvasBorderMode(0);
  snoStyle->SetPadBorderMode(0);
  snoStyle->SetPadBorderSize(0);
  snoStyle->SetPadColor(0);
  snoStyle->SetCanvasColor(0);
  snoStyle->SetTitleColor(0);
  snoStyle->SetStatColor(0);
  // snoStyle->SetFillColor(0); // needs to be commented out so that TPalette works on TH2

  // Use bold lines 
  snoStyle->SetHistLineWidth(2);
  snoStyle->SetLineWidth(2);

  // No title, stats box or fit as default
  snoStyle->SetOptTitle(0);
  snoStyle->SetOptStat(0);
  snoStyle->SetOptFit(0);
  
  // Postscript dashes
  snoStyle->SetLineStyleString(2,"[12 12]"); // postscript dashes

  // Text style and size
  snoStyle->SetLabelOffset(0.01,"x");
  snoStyle->SetTickLength(0.015,"x");
  snoStyle->SetTitleOffset(1.5,"x");
  snoStyle->SetLabelOffset(0.01,"y");
  snoStyle->SetTickLength(0.015,"y");
  snoStyle->SetTitleOffset(1.5,"y");
  snoStyle->SetLabelOffset(0.01,"z");
  snoStyle->SetTickLength(0.015,"z");
  snoStyle->SetTitleOffset(1.5,"z");
  snoStyle->SetLabelFont(132,"x");
  snoStyle->SetLabelFont(132,"y");
  snoStyle->SetLabelFont(132,"z");
  snoStyle->SetTitleFont(132,"x");
  snoStyle->SetTitleFont(132,"y");
  snoStyle->SetTitleFont(132,"z");
  snoStyle->SetLabelSize(0.05,"x");
  snoStyle->SetTitleSize(0.06,"x");
  snoStyle->SetTitleColor(1,"x");
  snoStyle->SetLabelSize(0.05,"y");
  snoStyle->SetTitleSize(0.06,"y");
  snoStyle->SetTitleColor(1,"y");
  snoStyle->SetLabelSize(0.05,"z");
  snoStyle->SetTitleSize(0.06,"z");
  snoStyle->SetTitleColor(1,"z");
  snoStyle->SetPadTickX(1);
  snoStyle->SetPadTickY(1);

  // Axis Offsets
  snoStyle->SetTitleOffset(0.8,"x");
  snoStyle->SetTitleOffset(0.8,"y");
  snoStyle->SetTitleOffset(0.8,"z");

  // Legends
  snoStyle->SetLegendBorderSize(0);
  snoStyle->SetLegendFont(132);
  snoStyle->SetLegendFillColor(0);
    
  // Graphs - set default marker to filled square
  snoStyle->SetMarkerStyle(21);

  // Palette for TH2 plots
  // Please try to use a Colour Vision Deficiency (CVD) friendly palettes. 
  // You can make your own or use one of the ROOT pre-defined palettes on https://root.cern.ch/doc/master/classTColor.html
  snoStyle->SetPalette(kInvertedDarkBodyRadiator);
    
  // SNO+ Preliminary label
  snoStyle->SetTextFont(132);
  snoStyle->SetTextSize(0.06);
  snoStyle->SetTextAlign(32); // Right (horizontally) and center (vertically) adjusted

  gROOT->SetStyle("snoplus");
  // gROOT->ForceStyle(); // Sometimes this line is necessary to force the figures to use the defined style

  ////              ////
  ////   TCanvas    ////
  ////              ////
  // It is useful to define a TCanvas where your figure will be displayed
  // The canvas can be saved into a pdf file
  // Configuring the canvas also allows to specify the aspect ratio (h:w) of the figure
  TCanvas *c1 = new TCanvas("c1","c1");
  // Options for a 16:9 aspect ratio (more rectangular)
  //Double_t width = 1600; // Width of the TCanvas
  //Double_t height = 900; // Height of the TCanvas
  // Options for a 4:3 aspect ratio (more squared)
  Double_t width = 800; // Width of the TCanvas
  Double_t height = 600; // Height of the TCanvas
  c1->SetCanvasSize(width,height);
  c1->SetWindowSize(width + (width - c1->GetWw()), height + (height - c1->GetWh()));
  c1->SetLeftMargin(0.2);
  c1->SetBottomMargin(0.2);
  c1->cd();
  
  ////               ////
  ////   Example 1   ////
  ////               ////

  // Function
  TF1 *f = new TF1("f","gaus",0,1);
  f->SetParameters(1,0,0.5);
  f->GetXaxis()->SetTitle("#beta_{14}");
  f->GetYaxis()->SetTitle("R^{3} / R_{AV}^{3}");
  f->SetLineColor(kRed);
  f->Draw();

  // Histogram
  TH1F *h = new TH1F("h","h",10,0,1);
  h->FillRandom("f",100);
  h->SetLineColor(kBlue);
  h->Scale(0.05);
  h->Draw("histo,same");

  // Graph with error bars
  float a[4] = {0.1,0.4,0.6,0.8};
  float b[4] = {0.6,0.5,0.4,0.3};
  float berr[4] = {0.05,0.05,0.05,0.05};
  TGraphErrors *g = new TGraphErrors(4,a,b,0,berr);
  g->SetName("g");
  g->SetMarkerColor(kBlack);
  g->Draw("P,same");

  // Draw the legend
  TLegend *leg = new TLegend(0.7,0.7,0.89,0.89);
  leg->AddEntry("f","Gaussian Fit","L");
  leg->AddEntry("h","MC histo","L");
  leg->AddEntry("g","Data points","PL");
  leg->Draw("same");

  // Draw the SNO+ Preliminary mandatory label
  TText *tPrelim = new TText(0.88,0.65,"SNO+ Preliminary");
  tPrelim->SetNDC();
  tPrelim->Draw("same");

  ////               ////
  ////   Example 2   ////
  ////               ////

  // 2D contour plots
  TCanvas *c2 = new TCanvas("c2","c2");
  // Using the same aspect ratio of TCanvas c1
  c2->SetCanvasSize(width,height);
  c2->SetWindowSize(width + (width - c2->GetWw()), height + (height - c2->GetWh()));
  c2->SetRightMargin(0.2);
  c2->SetLeftMargin(0.2);
  c2->SetBottomMargin(0.2);
  c2->cd();

  TH2F *h2 = new TH2F("h2","",40,-4.0,4.0,40,-20.0,20.0);
  TF2 *f2 = new TF2("f2","x^2+y^2",-4.0,4.0,-4.0,4.0);
  h2->FillRandom("f2");
  h2->GetXaxis()->SetTitle("X^{2} (mm)");
  h2->GetYaxis()->SetTitle("Y^{2} (mm)");
  h2->GetZaxis()->SetTitle("Counts");
  h2->Draw("COLZ");

  // Draw the SNO+ Preliminary mandatory label
  TText *tPrelim2 = new TText(0.78,0.5,"SNO+ Preliminary");
  tPrelim2->SetNDC();
  tPrelim2->Draw("same");

  ////                ////
  ////   Save Plots   ////
  ////                ////
  c1->SaveAs("example1D.pdf");
  c2->SaveAs("example2D.pdf");
  
}
