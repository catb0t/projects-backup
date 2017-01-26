#!/usr/bin/env perl6
use GTK::Simple;

my GTK::Simple::App $app .= new;
$app.border_width = 20;
$app.set_content(GTK::Simple::Label.new(text => "Goodbye, World!"));
$app.run;