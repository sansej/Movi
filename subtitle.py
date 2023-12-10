from moviepy.editor import TextClip
from moviepy.config import change_settings
import unicodedata

class SubtitleEditor:

    def create_subtitle_clips(subtitles, videosize,fontsize=80, xy_pos=('center',800),font='Arial', color='white', background = 'transparent', stroke_color= None, stroke_width = 1, debug = False):
        """
        Parameters
        -----------
        subtitles - SubRipFile array ``[<pysrt.srtitem.SubRipItem object at 0x000001A055A88530>]``

        output_path - path to modified image ``*.JPG`` ``*.PNG``

        resolution - final image resolution, default ``720*1280``
        """
        subtitle_clips = []
        change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16\\magick.exe"})
        for subtitle in subtitles:
            if isinstance(subtitle[0], float) or isinstance(subtitle[0], int):
                start_time = subtitle[0]
                end_time = subtitle[1]
            else:
                start_time = time_to_seconds(subtitle[0])
                end_time = time_to_seconds(subtitle[1])
            duration = end_time - start_time
            video_width, video_height = videosize
            text_clip = TextClip(subtitle[2], fontsize=fontsize, font=font, color=color, bg_color=background, stroke_color=stroke_color, stroke_width=stroke_width,size=(video_width*3/4, None), method='caption').set_start(start_time).set_duration(duration)
            # print ( text_clip.list("font") )
            subtitle_x_position = xy_pos[0]
            subtitle_y_position = xy_pos[1]
            text_position = (subtitle_x_position, subtitle_y_position)                    
            subtitle_clips.append(text_clip.set_position(text_position))
        return subtitle_clips

    def split_text(text, num_parts):
        """
        Parameters
        -----------
        text - text string

        num_parts - number of text parts
        """
        words = text.split()
        total_chars = len(text.replace(" ", ""))
        chars_per_part = round(total_chars / num_parts)
        current_part = 1
        text_parts = []
        old_part = 1
        word_box = ''
        simbol_counter=0
        current_chars = total_chars
        for word in words:
            ln = len([char for char in unicodedata.normalize('NFD', word) if unicodedata.category(char) != 'Mn'])
            if simbol_counter + ln <= round(chars_per_part*1.1):
                word_box = word_box + word + ' '
                simbol_counter += ln
            else:
                current_part += 1
                current_chars -= simbol_counter
                simbol_counter = ln
                text_parts.append(word_box + ' ')
                word_box = ''
                word_box = word_box + word + ' '
            if old_part!=current_part:
                chars_per_part = round(current_chars / (num_parts - old_part))
                old_part = current_part
        text_parts.append(word_box)
        return text_parts
    
def time_to_seconds(time_srt):
    """
    time_srt - format ``00:00:00,000``
    """
    time_h_m = time_srt.split(':')
    time_s_ms = time_h_m[2].split(',')
    return round(int(time_h_m[0]) * 3600 + int(time_h_m[1]) * 60 + int(time_s_ms[0]) + int(time_s_ms[1]) / 1000000, 3)

def len_simbols(file_path):
    total_chars = 0
    with open(file_path, 'r', encoding='UTF-8') as file:
        text = file.read()
        total_chars = len(text.replace(" ", ""))
        file.close()
    return total_chars

# ['AdobeArabic-Bold', 'AdobeArabic-BoldItalic', 'AdobeArabic-Italic', 'AdobeArabic-Regular', 'AdobeFanHeitiStd-Bold', 'AdobeGothicStd-Bold', 'AdobeHebrew-Bold', 'AdobeHebrew-BoldItalic', 'AdobeHebrew-Italic', 'AdobeHebrew-Regular', 'AdobeHeitiStd-Regular', 'AdobeMingStd-Light', 'AdobeMyungjoStd-Medium', 'AdobePiStd', 'AdobeSongStd-Light', 'AdobeThai-Bold', 'AdobeThai-BoldItalic', 'AdobeThai-Italic', 'AdobeThai-Regular', 'Agency-FB', 'Agency-FB-Pogrubiony', 'Algerian', 'Arial', 'Arial-Black', 'Arial-Bold', 'Arial-Bold-Italic', 'Arial-Italic', 'Arial-Narrow', 'Arial-Narrow-Kursywa', 'Arial-Narrow-Pogrubiona-kursywa', 'Arial-Narrow-Pogrubiony', 'Arial-Rounded-MT-Bold', 'Bahnschrift', 'Baskerville-Old-Face', 'Bauhaus-93', 'Bell-MT', 'Bell-MT-Kursywa', 'Bell-MT-Pogrubiony', 'Berlin-Sans-FB', 'Berlin-Sans-FB-Demi-Pogrubiony', 'Berlin-Sans-FB-Pogrubiony', 'Bernard-MT-Condensed', 'Blackadder-ITC', 'Bodoni-MT', 'Bodoni-MT-Black', 'Bodoni-MT-Black-Kursywa', 'Bodoni-MT-Condensed', 'Bodoni-MT-Condensed-Kursywa', 'Bodoni-MT-Condensed-Pogrubiona-kursywa', 'Bodoni-MT-Condensed-Pogrubiony', 'Bodoni-MT-Kursywa', 'Bodoni-MT-Pogrubiona-kursywa', 'Bodoni-MT-Pogrubiony', 'Bodoni-MT-Poster-Compressed', 'Book-Antiqua', 'Book-Antiqua-Kursywa', 'Book-Antiqua-Pogrubiona-kursywa', 'Book-Antiqua-Pogrubiony', 'Bookman-Old-Style', 'Bookman-Old-Style-Kursywa', 'Bookman-Old-Style-Pogrubiona-kursywa', 'Bookman-Old-Style-Pogrubiony', 'Bookshelf-Symbol-7', 'Bradley-Hand-ITC', 'Britannic-Bold', 'Broadway', 'Brush-Script-MT-Kursywa', 'Calibri', 'Calibri-Bold', 'Calibri-Bold-Italic', 'Calibri-Italic', 'Calibri-Light', 'Calibri-Light-Italic', 'Californian-FB', 'Californian-FB-Kursywa', 'Californian-FB-Pogrubiony', 'Calisto-MT', 'Calisto-MT-Kursywa', 'Calisto-MT-Pogrubiona-kursywa', 'Calisto-MT-Pogrubiony', 'Cambria-&-Cambria-Math', 'Cambria-Bold', 'Cambria-Bold-Italic', 'Cambria-Italic', 'Candara', 'Candara-Bold', 'Candara-Bold-Italic', 'Candara-Italic', 'Candara-Light', 'Candara-Light-Italic', 'Cascadia-Code-Regular', 'Cascadia-Mono-Regular', 'Castellar', 'CATIA-Symbols', 'Centaur', 'Century', 'Century-Gothic', 'Century-Gothic-Kursywa', 'Century-Gothic-Pogrubiona-kursywa', 'Century-Gothic-Pogrubiony', 'Century-Schoolbook', 'Century-Schoolbook-Kursywa', 'Century-Schoolbook-Pogrubiona-kursywa', 'Century-Schoolbook-Pogrubiony', 'Chiller', 'Colonna-MT', 'Comic-Sans-MS', 'Comic-Sans-MS-Bold', 'Comic-Sans-MS-Bold-Italic', 'Comic-Sans-MS-Italic', 'Consolas', 'Consolas-Bold', 'Consolas-Bold-Italic', 'Consolas-Italic', 'Constantia', 'Constantia-Bold', 'Constantia-Bold-Italic', 'Constantia-Italic', 'Cooper-Black', 'Copperplate-Gothic-Bold', 'Copperplate-Gothic-Light', 'Corbel', 'Corbel-Bold', 'Corbel-Bold-Italic', 'Corbel-Italic', 'Corbel-Light', 'Corbel-Light-Italic', 'Courier-10-Pitch-Bold-BT', 'Courier-10-Pitch-Bold-Italic-BT', 'Courier-10-Pitch-BT', 'Courier-10-Pitch-Italic-BT', 'Courier-New', 'Courier-New-Bold', 'Courier-New-Bold-Italic', 'Courier-New-Italic', 'CourierStd', 'CourierStd-Bold', 'CourierStd-BoldOblique', 'CourierStd-Oblique', 'Curlz-MT', 'Dubai-Bold', 'Dubai-Light', 'Dubai-Medium', 'Dubai-Regular', 'Dutch-801-Bold-BT', 'Dutch-801-Bold-Italic-BT', 'Dutch-801-Italic-BT', 'Dutch-801-Roman-BT', 'Ebrima', 'Ebrima-Bold', 'Edwardian-Script-ITC', 'Elephant', 'Elephant-Kursywa', 'Engravers-MT', 'Eras-Bold-ITC', 'Eras-Demi-ITC', 'Eras-Light-ITC', 'Eras-Medium-ITC', 'Felix-Titling', 'Footlight-MT-Light', 'Forte', 'Franklin-Gothic-Book', 'Franklin-Gothic-Book-Kursywa', 'Franklin-Gothic-Demi', 'Franklin-Gothic-Demi-Cond', 'Franklin-Gothic-Demi-Kursywa', 'Franklin-Gothic-Heavy', 'Franklin-Gothic-Heavy-Kursywa', 'Franklin-Gothic-Medium', 'Franklin-Gothic-Medium-Cond', 'Franklin-Gothic-Medium-Italic', 'Freestyle-Script', 'French-Script-MT', 'Gabriola', 'Gadugi', 'Gadugi-Bold', 'Garamond', 'Garamond-Kursywa', 'Garamond-Pogrubiony', 'Georgia', 'Georgia-Bold', 'Georgia-Bold-Italic', 'Georgia-Italic', 'Gigi', 'Gill-Sans-MT', 'Gill-Sans-MT-Condensed', 'Gill-Sans-MT-Ext-Condensed-Bold', 'Gill-Sans-MT-Kursywa', 'Gill-Sans-MT-Pogrubiona-kursywa', 'Gill-Sans-MT-Pogrubiony', 'Gill-Sans-Ultra-Bold', 'Gill-Sans-Ultra-Bold-Condensed', 'Gloucester-MT-Extra-Condensed', 'Goudy-Old-Style', 'Goudy-Old-Style-Kursywa', 'Goudy-Old-Style-Pogrubiony', 'Goudy-Stout', 'Haettenschweiler', 'Harlow-Solid-Italic', 'Harrington', 'High-Tower-Text', 'High-Tower-Text-Kursywa', 'Holo-MDL2-Assets', 'HYSWLongFangSong', 'Impact', 'Imprint-MT-Shadow', 'Informal-Roman', 'Ink-Free', 'Javanese-Text', 'Jokerman', 'Juice-ITC', 'KozGoPr6N-Medium', 'KozMinPr6N-Regular', 'Kristen-ITC', 'Kunstler-Script', 'Leelawadee-Pogrubiony', 'Leelawadee-UI', 'Leelawadee-UI-Bold', 'Leelawadee-UI-Semilight', 'Lucida-Bright', 'Lucida-Bright-Demibold', 'Lucida-Bright-Demibold-Italic', 'Lucida-Bright-Italic', 'Lucida-Calligraphy-Italic', 'Lucida-Console', 'Lucida-Fax-Demibold', 'Lucida-Fax-Demibold-Italic', 'Lucida-Fax-Italic', 'Lucida-Fax-Regular', 'Lucida-Handwriting-Italic', 'Lucida-Sans-Demibold-Italic', 'Lucida-Sans-Demibold-Roman', 'Lucida-Sans-Italic', 'Lucida-Sans-Regular', 'Lucida-Sans-Typewriter-Bold', 'Lucida-Sans-Typewriter-Bold-Oblique', 'Lucida-Sans-Typewriter-Oblique', 'Lucida-Sans-Typewriter-Regular', 'Lucida-Sans-Unicode', 'Magneto-Pogrubiony', 'Maiandra-GD', 'Malgun-Gothic', 'Malgun-Gothic-Bold', 'Malgun-Gothic-SemiLight', 'Matura-MT-Script-Capitals', 'Microsoft-Himalaya', 'Microsoft-JhengHei-&-Microsoft-JhengHei-UI', 'Microsoft-JhengHei-Bold-&-Microsoft-JhengHei-UI-Bold', 'Microsoft-JhengHei-Light-&-Microsoft-JhengHei-UI-Light', 'Microsoft-New-Tai-Lue', 'Microsoft-New-Tai-Lue-Bold', 'Microsoft-PhagsPa', 'Microsoft-PhagsPa-Bold', 'Microsoft-Sans-Serif', 'Microsoft-Tai-Le', 'Microsoft-Tai-Le-Bold', 'Microsoft-Uighur-Pogrubiony', 'Microsoft-YaHei-&-Microsoft-YaHei-UI', 'Microsoft-YaHei-Bold-&-Microsoft-YaHei-UI-Bold', 'Microsoft-YaHei-Light-&-Microsoft-YaHei-UI-Light', 'Microsoft-Yi-Baiti', 'MingLiU-ExtB-&-PMingLiU-ExtB-&-MingLiU_HKSCS-ExtB', 'MinionPro-Regular', 'Mistral', 'Modern-No.-20', 'Mongolian-Baiti', 'Monospace-821-Bold-BT', 'Monospace-821-Bold-Italic-BT', 'Monospace-821-BT', 'Monospace-821-Italic-BT', 'Monotype-Corsiva', 'MS-Gothic-&-MS-UI-Gothic-&-MS-PGothic', 'MS-Outlook', 'MS-Reference-Sans-Serif', 'MS-Reference-Specialty', 'MT-Extra', 'MV-Boli', 'Myanmar-Text', 'Myanmar-Text-Bold', 'MyriadCAD', 'MyriadPro-Regular', 'Niagara-Engraved', 'Niagara-Solid', 'Nirmala-UI', 'Nirmala-UI-Bold', 'Nirmala-UI-Semilight', 'OCR-A-Extended', 'Old-English-Text-MT', 'OLFSimpleSansOC-Regular', 'Onyx', 'Palace-Script-MT', 'Palatino-Linotype', 'Palatino-Linotype-Bold', 'Palatino-Linotype-Bold-Italic', 'Palatino-Linotype-Italic', 'Papyrus', 'Parchment', 'Perpetua', 'Perpetua-Kursywa', 'Perpetua-Pogrubiona-kursywa', 'Perpetua-Pogrubiony', 'Perpetua-Titling-MT-Light', 'Perpetua-Titling-MT-Pogrubiony', 'Playbill', 'Poor-Richard', 'Pristina', 'Rage-Italic', 'Ravie', 'Rockwell', 'Rockwell-Condensed', 'Rockwell-Condensed-Pogrubiony', 'Rockwell-Extra-Bold', 'Rockwell-Kursywa', 'Rockwell-Pogrubiona-kursywa', 'Rockwell-Pogrubiony', 'Sans-Serif-Collection', 'Script-MT-Bold', 'Segoe-Fluent-Icons', 'Segoe-MDL2-Assets', 'Segoe-Print', 'Segoe-Print-Bold', 'Segoe-Script', 'Segoe-Script-Bold', 'Segoe-UI', 'Segoe-UI-Black', 'Segoe-UI-Black-Italic', 'Segoe-UI-Bold', 'Segoe-UI-Bold-Italic', 'Segoe-UI-Emoji', 'Segoe-UI-Historic', 'Segoe-UI-Italic', 'Segoe-UI-Light', 'Segoe-UI-Light-Italic', 'Segoe-UI-Semibold', 'Segoe-UI-Semibold-Italic', 'Segoe-UI-Semilight', 'Segoe-UI-Semilight-Italic', 'Segoe-UI-Symbol', 'Segoe-UI-Variable', 'Showcard-Gothic', 'SimSun-&-NSimSun', 'SimSun-ExtB', 'Sitka-Text', 'Sitka-Text-Italic', 'Snap-ITC', 'Stencil', 'SWAstro', 'SWComp', 'SWGDT', 'SWGothe', 'SWGothg', 'SWGothi', 'SWGrekc', 'SWGreks', 'SWIsop1', 'SWIsop2', 'SWIsop3', 'SWIsot1', 'SWIsot2', 'SWIsot3', 'Swiss-721-Bold-BT', 'Swiss-721-Bold-Italic-BT', 'Swiss-721-Bold-Outline-BT', 'Swiss-721-BT', 'Swiss-721-Italic-BT', 'Swiss-721-Light-Condensed-BT', 'Swiss-721-Light-Condensed-Italic-BT', 'SWItal', 'SWItalc', 'SWItalt', 'SWLink', 'SWMap', 'SWMath', 'SWMeteo', 'SWMono', 'SWMusic', 'SWRomnc', 'SWRomnd', 'SWRomns', 'SWRomnt', 'SWScrpc', 'SWScrps', 'SWSimp', 'SWTxt', 'Sylfaen', 'Symbol', 'Symbol-Monospaced-BT', 'Symbol-Proportional-BT', 'Tahoma', 'Tahoma-Bold', 'Tempus-Sans-ITC', 'Times-New-Roman', 'Times-New-Roman-Bold', 'Times-New-Roman-Bold-Italic', 'Times-New-Roman-Italic', 'Trebuchet-MS', 'Trebuchet-MS-Bold', 'Trebuchet-MS-Bold-Italic', 'Trebuchet-MS-Italic', 'Tw-Cen-MT', 'Tw-Cen-MT-Condensed', 'Tw-Cen-MT-Condensed-Extra-Bold', 'Tw-Cen-MT-Condensed-Pogrubiony', 'Tw-Cen-MT-Kursywa', 'Tw-Cen-MT-Pogrubiona-kursywa', 'Tw-Cen-MT-Pogrubiony', 'Universal-Math-1-BT', 'Verdana', 'Verdana-Bold', 'Verdana-Bold-Italic', 'Verdana-Italic', 'Viner-Hand-ITC', 'Vivaldi-Kursywa', 'Vladimir-Script', 'Webdings', 'Wide-Latin', 'Wingdings', 'Wingdings-2', 'Wingdings-3', 'Yu-Gothic-Bold-&-Yu-Gothic-UI-Semibold-&-Yu-Gothic-UI-Bold', 'Yu-Gothic-Light-&-Yu-Gothic-UI-Light', 'Yu-Gothic-Medium-&-Yu-Gothic-UI-Regular', 'Yu-Gothic-Regular-&-Yu-Gothic-UI-Semilight']
    