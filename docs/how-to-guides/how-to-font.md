
# How to add font

Step by step guide to add a font:

## Step 1: Download font files

Go to a font repository like google fonts. Find a font that you want to add to the project. Download the fonts zip file.

<img src="docs/images/google-fonts.png" alt="Select font from google fonts" title="font_installation_1" width="75%">

## Step 2: Unpack the fonts into the project's data directory.

Open the report-generator's project directory or start a new project and then open it. Open the data directory and then open the fonts directory.

## Step 3: Copy the zip contents into the fonts directory.

Take the fonts zip file and unzip it. The contents should look similar to the image below.

<img src="docs/images/zipped_fonts.png" alt="Zipped fonts" title="font_installation_2" width="75%">

In the static directory there will be additional 'font.tff' files. Select the fonts that you want and copy the files into the fonts directory. Below is an example of what this might look like.

<img src="docs/images/font-types.png" alt="Fonts" title="font_installation_3" width="75%">

## Step 4: Update the fonts.yaml file.

The 'fonts.yaml' file lists the fonts that can be loaded by the report-generator program.

<img src="docs/images/fonts-yaml.png" alt="Fonts Yaml file" title="font_installation_4" width="75%">

There are two sections relevant to adding additional fonts:
1. font_types
2. custom_font_types

### Font Types

Font types are the default fonts that are build into the pdf file format. In the report-generator program we can select those fonts for any section of text in the outputted pdf report. They have built in options to supply a font with bold and italics. If we wanted to prevent the choice of using Symbol or Dingbats in our report output we would just delete those lines from the 'fonts.yaml' file and save it.

### Custom Font Types

Custom fonts are the fonts that we want to add. As they are not built in we need to supply both the standard font file but also the font files that we want to use for bold and italics text.

Therefore to add a font we need to:
1. Go to the bottom of the custom fonts section
2. Indent to match the fonts above and type in the name of the font.
3. Add a ':'
4. Take a new line and indent again.
5. Then provide like the picture the Normal, Italics and Bold font file names.

Save the 'fonts.yaml file' and re-open the report-generator program and the font selection should be updated.
