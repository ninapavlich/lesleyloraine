# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(null=True, verbose_name='admin note', blank=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name', blank=True)),
                ('middle_name', models.CharField(max_length=30, verbose_name='Middle name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name', blank=True)),
                ('date_of_birth', models.DateField(null=True, verbose_name='Date of Birth', blank=True)),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('about', models.TextField(help_text=b'', null=True, verbose_name='about', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(null=True, verbose_name='admin note', blank=True)),
                ('street_1', models.CharField(max_length=30, null=True, verbose_name='Street Address 1', blank=True)),
                ('street_2', models.CharField(max_length=30, null=True, verbose_name='Street Address 2', blank=True)),
                ('city', models.CharField(max_length=30, null=True, verbose_name='City', blank=True)),
                ('state', models.CharField(max_length=30, null=True, verbose_name='State', blank=True)),
                ('zipcode', models.CharField(max_length=30, null=True, verbose_name='Zipcode', blank=True)),
                ('latitude', models.CharField(max_length=30, null=True, verbose_name='Latitude', blank=True)),
                ('longitude', models.CharField(max_length=30, null=True, verbose_name='Longitude', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(null=True, verbose_name='admin note', blank=True)),
                ('title', models.CharField(help_text=b'The display title for this object.', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('slug', models.CharField(help_text=b'Auto-generated page slug for this object.', max_length=255, verbose_name='Slug', db_index=True, blank=True)),
                ('uuid', models.CharField(help_text=b'UUID generated for object; can be used for short URLs', max_length=255, verbose_name='UUID', blank=True)),
                ('order', models.IntegerField(default=0, help_text=b'')),
                ('path', models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='path', blank=True)),
                ('title_path', models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True)),
                ('path_generated', models.CharField(help_text=b'The URL path to this page, based on page hierarchy and slug.', max_length=255, null=True, verbose_name='generated path', blank=True)),
                ('path_override', models.CharField(help_text=b'The URL path to this page, defined absolutely.', max_length=255, null=True, verbose_name='path override', blank=True)),
                ('hierarchy', models.CharField(null=True, max_length=255, blank=True, help_text=b'Administrative Hierarchy', unique=True, verbose_name='hierarchy')),
                ('temporary_redirect', models.CharField(help_text=b'Temporarily redirect to a different path', max_length=255, verbose_name='Temporary Redirect', blank=True)),
                ('permanent_redirect', models.CharField(help_text=b'Permanently redirect to a different path', max_length=255, verbose_name='Permanent Redirect', blank=True)),
                ('publication_date', models.DateTimeField(null=True, verbose_name='Publication Date', blank=True)),
                ('publication_status', models.IntegerField(default=10, help_text=b'Current publication status', choices=[(10, 'Draft'), (20, 'Needs Review'), (100, 'Published'), (40, 'Unpublished')])),
                ('publish_on_date', models.DateTimeField(help_text=b"Object state will be set to 'Published' on this date.", null=True, verbose_name='Publish on Date', blank=True)),
                ('expire_on_date', models.DateTimeField(help_text=b"Object state will be set to 'Expired' on this date.", null=True, verbose_name='Expire on Date', blank=True)),
                ('page_meta_description', models.CharField(help_text=b'A short description of the page, used for SEO and not displayed to the user; aim for 150-160 characters.', max_length=2000, verbose_name='Meta Description', blank=True)),
                ('page_meta_keywords', models.CharField(help_text=b'A short list of keywords of the page, used for SEO and not displayed to the user; aim for 150-160 characters.', max_length=2000, verbose_name='Meta Page Keywords', blank=True)),
                ('is_searchable', models.BooleanField(default=True, help_text=b'Allow search engines to index this object and display in sitemap.')),
                ('in_sitemap', models.BooleanField(default=True, help_text=b'Is in sitemap')),
                ('noindex', models.BooleanField(default=False, help_text=b'Robots noindex')),
                ('nofollow', models.BooleanField(default=False, help_text=b'Robots nofollow')),
                ('sitemap_changefreq', models.CharField(default=b'monthly', help_text=b'How frequently does page content update', max_length=255, verbose_name='Sitemap Change Frequency', choices=[(b'never', 'Never'), (b'yearly', 'Yearly'), (b'monthly', 'Monthly'), (b'weekly', 'Weekly'), (b'daily', 'Daily'), (b'hourly', 'Hourly'), (b'always', 'Always')])),
                ('sitemap_priority', models.CharField(default=b'0.5', max_length=255, blank=True, help_text=b'Sitemap priority', null=True, verbose_name=b'Sitemap Priority')),
                ('shareable', models.BooleanField(default=False, help_text=b'Show sharing widget')),
                ('tiny_url', models.CharField(help_text=b'Tiny URL used for social sharing', max_length=255, null=True, verbose_name='tiny url', blank=True)),
                ('social_share_type', models.CharField(default=b'article', choices=[(b'article', b'Article'), (b'book', b'Book'), (b'profile', b'Profile'), (b'website', b'Website'), (b'video.movie', b'Video - Movie'), (b'video.episode', b'Video - Episode'), (b'video.tv_show', b'Video - TV Show'), (b'video.other', b'Video - Other'), (b'music.song', b'Music - Song'), (b'music.album', b'Music - Album'), (b'music.radio_station', b'Music - Playlist'), (b'music.radio_station', b'Music - Radio Station')], max_length=255, blank=True, null=True, verbose_name=b'Social type')),
                ('facebook_author_id', models.CharField(help_text=b'Numeric Facebook ID', max_length=255, null=True, verbose_name=b'Facebook Author ID', blank=True)),
                ('twitter_author_id', models.CharField(help_text=b'Twitter handle, including "@" e.g. @cgpartners', max_length=255, null=True, verbose_name=b'Twitter Admin ID', blank=True)),
                ('google_author_id', models.CharField(help_text=b'Google author id, e.g. the AUTHOR_ID in https://plus.google.com/AUTHOR_ID/posts', max_length=255, null=True, verbose_name=b'Google Admin ID', blank=True)),
                ('content', models.TextField(help_text=b'', null=True, verbose_name='content', blank=True)),
                ('synopsis', models.TextField(help_text=b'', null=True, verbose_name='synopsis', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(null=True, verbose_name='admin note', blank=True)),
                ('access', models.IntegerField(help_text=b'Access level', choices=[(10, 'Owner'), (20, 'Can Edit'), (30, 'Can View')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SocialContactLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(null=True, verbose_name='admin note', blank=True)),
                ('title', models.CharField(help_text=b'The display title for this object.', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('slug', models.CharField(help_text=b'Auto-generated page slug for this object.', max_length=255, verbose_name='Slug', db_index=True, blank=True)),
                ('order', models.IntegerField(default=0, help_text=b'')),
                ('url', models.CharField(max_length=255, null=True, verbose_name='URL', blank=True)),
                ('icon', models.CharField(blank=True, max_length=255, null=True, help_text=b'Preview icons at http://fontawesome.io/icons/', choices=[(b'glass', b'Glass'), (b'music', b'Music'), (b'search', b'Search'), (b'envelope-o', b'Envelope O'), (b'heart', b'Heart'), (b'star', b'Star'), (b'star-o', b'Star o'), (b'user', b'User'), (b'film', b'Film'), (b'th-large', b'Th Large'), (b'th', b'Th'), (b'th-list', b'Th List'), (b'check', b'Check'), (b'remove', b'Remove'), (b'close', b'Close'), (b'times', b'Times'), (b'search-plus', b'Search Plus'), (b'search-minus', b'Search Minus'), (b'power-off', b'Power Off'), (b'signal', b'Signal'), (b'gear', b'Gear'), (b'cog', b'Cog'), (b'trash-o', b'Trash o'), (b'home', b'Home'), (b'file-o', b'File o'), (b'clock-o', b'Clock o'), (b'road', b'Road'), (b'download', b'Download'), (b'arrow-circle-o-down', b'Arrow circle-o Down'), (b'arrow-circle-o-up', b'Arrow circle-o Up'), (b'inbox', b'Inbox'), (b'play-circle-o', b'Play circle o'), (b'rotate-right', b'Rotate Right'), (b'repeat', b'Repeat'), (b'refresh', b'Refresh'), (b'list-alt', b'List Alt'), (b'lock', b'Lock'), (b'flag', b'Flag'), (b'headphones', b'Headphones'), (b'volume-off', b'Volume Off'), (b'volume-down', b'Volume Down'), (b'volume-up', b'Volume Up'), (b'qrcode', b'Qrcode'), (b'barcode', b'Barcode'), (b'tag', b'Tag'), (b'tags', b'Tags'), (b'book', b'Book'), (b'bookmark', b'Bookmark'), (b'print', b'Print'), (b'camera', b'Camera'), (b'font', b'Font'), (b'bold', b'Bold'), (b'italic', b'Italic'), (b'text-height', b'Text Height'), (b'text-width', b'Text Width'), (b'align-left', b'Align Left'), (b'align-center', b'Align Center'), (b'align-right', b'Align Right'), (b'align-justify', b'Align Justify'), (b'list', b'List'), (b'dedent', b'Dedent'), (b'outdent', b'Outdent'), (b'indent', b'Indent'), (b'video-camera', b'Video Camera'), (b'photo', b'Photo'), (b'image', b'Image'), (b'picture-o', b'Picture o'), (b'pencil', b'Pencil'), (b'map-marker', b'Map Marker'), (b'adjust', b'Adjust'), (b'tint', b'Tint'), (b'edit', b'Edit'), (b'pencil-square-o', b'Pencil square o'), (b'share-square-o', b'Share square o'), (b'check-square-o', b'Check square o'), (b'arrows', b'Arrows'), (b'step-backward', b'Step Backward'), (b'fast-backward', b'Fast Backward'), (b'backward', b'Backward'), (b'play', b'Play'), (b'pause', b'Pause'), (b'stop', b'Stop'), (b'forward', b'Forward'), (b'fast-forward', b'Fast Forward'), (b'step-forward', b'Step Forward'), (b'eject', b'Eject'), (b'chevron-left', b'Chevron Left'), (b'chevron-right', b'Chevron Right'), (b'plus-circle', b'Plus Circle'), (b'minus-circle', b'Minus Circle'), (b'times-circle', b'Times Circle'), (b'check-circle', b'Check Circle'), (b'question-circle', b'Question Circle'), (b'info-circle', b'Info Circle'), (b'crosshairs', b'Crosshairs'), (b'times-circle-o', b'Times circle o'), (b'check-circle-o', b'Check circle o'), (b'ban', b'Ban'), (b'arrow-left', b'Arrow Left'), (b'arrow-right', b'Arrow Right'), (b'arrow-up', b'Arrow Up'), (b'arrow-down', b'Arrow Down'), (b'mail-forward', b'Mail Forward'), (b'share', b'Share'), (b'expand', b'Expand'), (b'compress', b'Compress'), (b'plus', b'Plus'), (b'minus', b'Minus'), (b'asterisk', b'Asterisk'), (b'exclamation-circle', b'Exclamation Circle'), (b'gift', b'Gift'), (b'leaf', b'Leaf'), (b'fire', b'Fire'), (b'eye', b'Eye'), (b'eye-slash', b'Eye Slash'), (b'warning', b'Warning'), (b'exclamation-triangle', b'Exclamation Triangle'), (b'plane', b'Plane'), (b'calendar', b'Calendar'), (b'random', b'Random'), (b'comment', b'Comment'), (b'magnet', b'Magnet'), (b'chevron-up', b'Chevron Up'), (b'chevron-down', b'Chevron Down'), (b'retweet', b'Retweet'), (b'shopping-cart', b'Shopping Cart'), (b'folder', b'Folder'), (b'folder-open', b'Folder Open'), (b'arrows-v', b'Arrows v'), (b'arrows-h', b'Arrows h'), (b'bar-chart-o', b'Bar chart o'), (b'bar-chart', b'Bar Chart'), (b'twitter-square', b'Twitter Square'), (b'facebook-square', b'Facebook Square'), (b'camera-retro', b'Camera Retro'), (b'key', b'Key'), (b'gears', b'Gears'), (b'cogs', b'Cogs'), (b'comments', b'Comments'), (b'thumbs-o-up', b'Thumbs o Up'), (b'thumbs-o-down', b'Thumbs o Down'), (b'star-half', b'Star Half'), (b'heart-o', b'Heart o'), (b'sign-out', b'Sign Out'), (b'linkedin-square', b'Linkedin Square'), (b'thumb-tack', b'Thumb Tack'), (b'external-link', b'External Link'), (b'sign-in', b'Sign In'), (b'trophy', b'Trophy'), (b'github-square', b'Github Square'), (b'upload', b'Upload'), (b'lemon-o', b'Lemon o'), (b'phone', b'Phone'), (b'square-o', b'Square o'), (b'bookmark-o', b'Bookmark o'), (b'phone-square', b'Phone Square'), (b'twitter', b'Twitter'), (b'facebook-f', b'Facebook f'), (b'facebook', b'Facebook'), (b'github', b'Github'), (b'unlock', b'Unlock'), (b'credit-card', b'Credit Card'), (b'rss', b'Rss'), (b'hdd-o', b'Hdd o'), (b'bullhorn', b'Bullhorn'), (b'bell', b'Bell'), (b'certificate', b'Certificate'), (b'hand-o-right', b'Hand o Right'), (b'hand-o-left', b'Hand o Left'), (b'hand-o-up', b'Hand o Up'), (b'hand-o-down', b'Hand o Down'), (b'arrow-circle-left', b'Arrow circle Left'), (b'arrow-circle-right', b'Arrow circle Right'), (b'arrow-circle-up', b'Arrow circle Up'), (b'arrow-circle-down', b'Arrow circle Down'), (b'globe', b'Globe'), (b'wrench', b'Wrench'), (b'tasks', b'Tasks'), (b'filter', b'Filter'), (b'briefcase', b'Briefcase'), (b'arrows-alt', b'Arrows Alt'), (b'group', b'Group'), (b'users', b'Users'), (b'chain', b'Chain'), (b'link', b'Link'), (b'cloud', b'Cloud'), (b'flask', b'Flask'), (b'cut', b'Cut'), (b'scissors', b'Scissors'), (b'copy', b'Copy'), (b'files-o', b'Files o'), (b'paperclip', b'Paperclip'), (b'save', b'Save'), (b'floppy-o', b'Floppy o'), (b'square', b'Square'), (b'navicon', b'Navicon'), (b'reorder', b'Reorder'), (b'bars', b'Bars'), (b'list-ul', b'List Ul'), (b'list-ol', b'List Ol'), (b'strikethrough', b'Strikethrough'), (b'underline', b'Underline'), (b'table', b'Table'), (b'magic', b'Magic'), (b'truck', b'Truck'), (b'pinterest', b'Pinterest'), (b'pinterest-square', b'Pinterest Square'), (b'google-plus-square', b'Google plus Square'), (b'google-plus', b'Google Plus'), (b'money', b'Money'), (b'caret-down', b'Caret Down'), (b'caret-up', b'Caret Up'), (b'caret-left', b'Caret Left'), (b'caret-right', b'Caret Right'), (b'columns', b'Columns'), (b'unsorted', b'Unsorted'), (b'sort', b'Sort'), (b'sort-down', b'Sort Down'), (b'sort-desc', b'Sort Desc'), (b'sort-up', b'Sort Up'), (b'sort-asc', b'Sort Asc'), (b'envelope', b'Envelope'), (b'linkedin', b'Linkedin'), (b'rotate-left', b'Rotate Left'), (b'undo', b'Undo'), (b'legal', b'Legal'), (b'gavel', b'Gavel'), (b'dashboard', b'Dashboard'), (b'tachometer', b'Tachometer'), (b'comment-o', b'Comment o'), (b'comments-o', b'Comments o'), (b'flash', b'Flash'), (b'bolt', b'Bolt'), (b'sitemap', b'Sitemap'), (b'umbrella', b'Umbrella'), (b'paste', b'Paste'), (b'clipboard', b'Clipboard'), (b'lightbulb-o', b'Lightbulb o'), (b'exchange', b'Exchange'), (b'cloud-download', b'Cloud Download'), (b'cloud-upload', b'Cloud Upload'), (b'user-md', b'User Md'), (b'stethoscope', b'Stethoscope'), (b'suitcase', b'Suitcase'), (b'bell-o', b'Bell o'), (b'coffee', b'Coffee'), (b'cutlery', b'Cutlery'), (b'file-text-o', b'File text o'), (b'building-o', b'Building o'), (b'hospital-o', b'Hospital o'), (b'ambulance', b'Ambulance'), (b'medkit', b'Medkit'), (b'fighter-jet', b'Fighter Jet'), (b'beer', b'Beer'), (b'h-square', b'h Square'), (b'plus-square', b'Plus Square'), (b'angle-double-left', b'Angle double Left'), (b'angle-double-right', b'Angle double Right'), (b'angle-double-up', b'Angle double Up'), (b'angle-double-down', b'Angle double Down'), (b'angle-left', b'Angle Left'), (b'angle-right', b'Angle Right'), (b'angle-up', b'Angle Up'), (b'angle-down', b'Angle Down'), (b'desktop', b'Desktop'), (b'laptop', b'Laptop'), (b'tablet', b'Tablet'), (b'mobile-phone', b'Mobile Phone'), (b'mobile', b'Mobile'), (b'circle-o', b'Circle o'), (b'quote-left', b'Quote Left'), (b'quote-right', b'Quote Right'), (b'spinner', b'Spinner'), (b'circle', b'Circle'), (b'mail-reply', b'Mail Reply'), (b'reply', b'Reply'), (b'github-alt', b'Github Alt'), (b'folder-o', b'Folder o'), (b'folder-open-o', b'Folder open o'), (b'smile-o', b'Smile o'), (b'frown-o', b'Frown o'), (b'meh-o', b'Meh o'), (b'gamepad', b'Gamepad'), (b'keyboard-o', b'Keyboard o'), (b'flag-o', b'Flag o'), (b'flag-checkered', b'Flag Checkered'), (b'terminal', b'Terminal'), (b'code', b'Code'), (b'mail-reply-all', b'Mail reply All'), (b'reply-all', b'Reply All'), (b'star-half-empty', b'Star half Empty'), (b'star-half-full', b'Star half Full'), (b'star-half-o', b'Star half o'), (b'location-arrow', b'Location Arrow'), (b'crop', b'Crop'), (b'code-fork', b'Code Fork'), (b'unlink', b'Unlink'), (b'chain-broken', b'Chain Broken'), (b'question', b'Question'), (b'info', b'Info'), (b'exclamation', b'Exclamation'), (b'superscript', b'Superscript'), (b'subscript', b'Subscript'), (b'eraser', b'Eraser'), (b'puzzle-piece', b'Puzzle Piece'), (b'microphone', b'Microphone'), (b'microphone-slash', b'Microphone Slash'), (b'shield', b'Shield'), (b'calendar-o', b'Calendar o'), (b'fire-extinguisher', b'Fire Extinguisher'), (b'rocket', b'Rocket'), (b'maxcdn', b'Maxcdn'), (b'chevron-circle-left', b'Chevron circle Left'), (b'chevron-circle-right', b'Chevron circle Right'), (b'chevron-circle-up', b'Chevron circle Up'), (b'chevron-circle-down', b'Chevron circle Down'), (b'html5', b'Html5'), (b'css3', b'Css3'), (b'anchor', b'Anchor'), (b'unlock-alt', b'Unlock Alt'), (b'bullseye', b'Bullseye'), (b'ellipsis-h', b'Ellipsis h'), (b'ellipsis-v', b'Ellipsis v'), (b'rss-square', b'Rss Square'), (b'play-circle', b'Play Circle'), (b'ticket', b'Ticket'), (b'minus-square', b'Minus Square'), (b'minus-square-o', b'Minus square o'), (b'level-up', b'Level Up'), (b'level-down', b'Level Down'), (b'check-square', b'Check Square'), (b'pencil-square', b'Pencil Square'), (b'external-link-square', b'External link Square'), (b'share-square', b'Share Square'), (b'compass', b'Compass'), (b'toggle-down', b'Toggle Down'), (b'caret-square-o-down', b'Caret square-o Down'), (b'toggle-up', b'Toggle Up'), (b'caret-square-o-up', b'Caret square-o Up'), (b'toggle-right', b'Toggle Right'), (b'caret-square-o-right', b'Caret square-o Right'), (b'euro', b'Euro'), (b'eur', b'Eur'), (b'gbp', b'Gbp'), (b'dollar', b'Dollar'), (b'usd', b'Usd'), (b'rupee', b'Rupee'), (b'inr', b'Inr'), (b'cny', b'Cny'), (b'rmb', b'Rmb'), (b'yen', b'Yen'), (b'jpy', b'Jpy'), (b'ruble', b'Ruble'), (b'rouble', b'Rouble'), (b'rub', b'Rub'), (b'won', b'Won'), (b'krw', b'Krw'), (b'bitcoin', b'Bitcoin'), (b'btc', b'Btc'), (b'file', b'File'), (b'file-text', b'File Text'), (b'sort-alpha-asc', b'Sort alpha Asc'), (b'sort-alpha-desc', b'Sort alpha Desc'), (b'sort-amount-asc', b'Sort amount Asc'), (b'sort-amount-desc', b'Sort amount Desc'), (b'sort-numeric-asc', b'Sort numeric Asc'), (b'sort-numeric-desc', b'Sort numeric Desc'), (b'thumbs-up', b'Thumbs Up'), (b'thumbs-down', b'Thumbs Down'), (b'youtube-square', b'Youtube Square'), (b'youtube', b'Youtube'), (b'xing', b'Xing'), (b'xing-square', b'Xing Square'), (b'youtube-play', b'Youtube Play'), (b'dropbox', b'Dropbox'), (b'stack-overflow', b'Stack Overflow'), (b'instagram', b'Instagram'), (b'flickr', b'Flickr'), (b'adn', b'Adn'), (b'bitbucket', b'Bitbucket'), (b'bitbucket-square', b'Bitbucket Square'), (b'tumblr', b'Tumblr'), (b'tumblr-square', b'Tumblr Square'), (b'long-arrow-down', b'Long arrow Down'), (b'long-arrow-up', b'Long arrow Up'), (b'long-arrow-left', b'Long arrow Left'), (b'long-arrow-right', b'Long arrow Right'), (b'apple', b'Apple'), (b'windows', b'Windows'), (b'android', b'Android'), (b'linux', b'Linux'), (b'dribbble', b'Dribbble'), (b'skype', b'Skype'), (b'foursquare', b'Foursquare'), (b'trello', b'Trello'), (b'female', b'Female'), (b'male', b'Male'), (b'gittip', b'Gittip'), (b'gratipay', b'Gratipay'), (b'sun-o', b'Sun o'), (b'moon-o', b'Moon o'), (b'archive', b'Archive'), (b'bug', b'Bug'), (b'vk', b'Vk'), (b'weibo', b'Weibo'), (b'renren', b'Renren'), (b'pagelines', b'Pagelines'), (b'stack-exchange', b'Stack Exchange'), (b'arrow-circle-o-right', b'Arrow circle-o Right'), (b'arrow-circle-o-left', b'Arrow circle-o Left'), (b'toggle-left', b'Toggle Left'), (b'caret-square-o-left', b'Caret square-o Left'), (b'dot-circle-o', b'Dot circle o'), (b'wheelchair', b'Wheelchair'), (b'vimeo-square', b'Vimeo Square'), (b'turkish-lira', b'Turkish Lira'), (b'try', b'Try'), (b'plus-square-o', b'Plus square o'), (b'space-shuttle', b'Space Shuttle'), (b'slack', b'Slack'), (b'envelope-square', b'Envelope Square'), (b'wordpress', b'Wordpress'), (b'openid', b'Openid'), (b'institution', b'Institution'), (b'bank', b'Bank'), (b'university', b'University'), (b'mortar-board', b'Mortar Board'), (b'graduation-cap', b'Graduation Cap'), (b'yahoo', b'Yahoo'), (b'google', b'Google'), (b'reddit', b'Reddit'), (b'reddit-square', b'Reddit Square'), (b'stumbleupon-circle', b'Stumbleupon Circle'), (b'stumbleupon', b'Stumbleupon'), (b'delicious', b'Delicious'), (b'digg', b'Digg'), (b'pied-piper', b'Pied Piper'), (b'pied-piper-alt', b'Pied piper Alt'), (b'drupal', b'Drupal'), (b'joomla', b'Joomla'), (b'language', b'Language'), (b'fax', b'Fax'), (b'building', b'Building'), (b'child', b'Child'), (b'paw', b'Paw'), (b'spoon', b'Spoon'), (b'cube', b'Cube'), (b'cubes', b'Cubes'), (b'behance', b'Behance'), (b'behance-square', b'Behance Square'), (b'steam', b'Steam'), (b'steam-square', b'Steam Square'), (b'recycle', b'Recycle'), (b'automobile', b'Automobile'), (b'car', b'Car'), (b'cab', b'Cab'), (b'taxi', b'Taxi'), (b'tree', b'Tree'), (b'spotify', b'Spotify'), (b'deviantart', b'Deviantart'), (b'soundcloud', b'Soundcloud'), (b'database', b'Database'), (b'file-pdf-o', b'File pdf o'), (b'file-word-o', b'File word o'), (b'file-excel-o', b'File excel o'), (b'file-powerpoint-o', b'File powerpoint o'), (b'file-photo-o', b'File photo o'), (b'file-picture-o', b'File picture o'), (b'file-image-o', b'File image o'), (b'file-zip-o', b'File zip o'), (b'file-archive-o', b'File archive o'), (b'file-sound-o', b'File sound o'), (b'file-audio-o', b'File audio o'), (b'file-movie-o', b'File movie o'), (b'file-video-o', b'File video o'), (b'file-code-o', b'File code o'), (b'vine', b'Vine'), (b'codepen', b'Codepen'), (b'jsfiddle', b'Jsfiddle'), (b'life-bouy', b'Life Bouy'), (b'life-buoy', b'Life Buoy'), (b'life-saver', b'Life Saver'), (b'support', b'Support'), (b'life-ring', b'Life Ring'), (b'circle-o-notch', b'Circle o Notch'), (b'ra', b'Ra'), (b'rebel', b'Rebel'), (b'ge', b'Ge'), (b'empire', b'Empire'), (b'git-square', b'Git Square'), (b'git', b'Git'), (b'hacker-news', b'Hacker News'), (b'tencent-weibo', b'Tencent Weibo'), (b'qq', b'Qq'), (b'wechat', b'Wechat'), (b'weixin', b'Weixin'), (b'send', b'Send'), (b'paper-plane', b'Paper Plane'), (b'send-o', b'Send o'), (b'paper-plane-o', b'Paper plane o'), (b'history', b'History'), (b'genderless', b'Genderless'), (b'circle-thin', b'Circle Thin'), (b'header', b'Header'), (b'paragraph', b'Paragraph'), (b'sliders', b'Sliders'), (b'share-alt', b'Share Alt'), (b'share-alt-square', b'Share alt Square'), (b'bomb', b'Bomb'), (b'soccer-ball-o', b'Soccer ball o'), (b'futbol-o', b'Futbol o'), (b'tty', b'Tty'), (b'binoculars', b'Binoculars'), (b'plug', b'Plug'), (b'slideshare', b'Slideshare'), (b'twitch', b'Twitch'), (b'yelp', b'Yelp'), (b'newspaper-o', b'Newspaper o'), (b'wifi', b'Wifi'), (b'calculator', b'Calculator'), (b'paypal', b'Paypal'), (b'google-wallet', b'Google Wallet'), (b'cc-visa', b'Cc Visa'), (b'cc-mastercard', b'Cc Mastercard'), (b'cc-discover', b'Cc Discover'), (b'cc-amex', b'Cc Amex'), (b'cc-paypal', b'Cc Paypal'), (b'cc-stripe', b'Cc Stripe'), (b'bell-slash', b'Bell Slash'), (b'bell-slash-o', b'Bell slash o'), (b'trash', b'Trash'), (b'copyright', b'Copyright'), (b'at', b'At'), (b'eyedropper', b'Eyedropper'), (b'paint-brush', b'Paint Brush'), (b'birthday-cake', b'Birthday Cake'), (b'area-chart', b'Area Chart'), (b'pie-chart', b'Pie Chart'), (b'line-chart', b'Line Chart'), (b'lastfm', b'Lastfm'), (b'lastfm-square', b'Lastfm Square'), (b'toggle-off', b'Toggle Off'), (b'toggle-on', b'Toggle On'), (b'bicycle', b'Bicycle'), (b'bus', b'Bus'), (b'ioxhost', b'Ioxhost'), (b'angellist', b'Angellist'), (b'cc', b'Cc'), (b'shekel', b'Shekel'), (b'sheqel', b'Sheqel'), (b'ils', b'Ils'), (b'meanpath', b'Meanpath'), (b'buysellads', b'Buysellads'), (b'connectdevelop', b'Connectdevelop'), (b'dashcube', b'Dashcube'), (b'forumbee', b'Forumbee'), (b'leanpub', b'Leanpub'), (b'sellsy', b'Sellsy'), (b'shirtsinbulk', b'Shirtsinbulk'), (b'simplybuilt', b'Simplybuilt'), (b'skyatlas', b'Skyatlas'), (b'cart-plus', b'Cart Plus'), (b'cart-arrow-down', b'Cart arrow Down'), (b'diamond', b'Diamond'), (b'ship', b'Ship'), (b'user-secret', b'User Secret'), (b'motorcycle', b'Motorcycle'), (b'street-view', b'Street View'), (b'heartbeat', b'\\U$1\\L$2'), (b'venus', b'Venus'), (b'mars', b'Mars'), (b'mercury', b'Mercury'), (b'transgender', b'Transgender'), (b'transgender-alt', b'Transgender Alt'), (b'venus-double', b'Venus Double'), (b'mars-double', b'Mars Double'), (b'venus-mars', b'Venus Mars'), (b'mars-stroke', b'Mars Stroke'), (b'mars-stroke-v', b'Mars stroke v'), (b'mars-stroke-h', b'Mars stroke h'), (b'neuter', b'Neuter'), (b'facebook-official', b'Facebook Official'), (b'pinterest-p', b'Pinterest p'), (b'whatsapp', b'Whatsapp'), (b'server', b'Server'), (b'user-plus', b'User Plus'), (b'user-times', b'User Times'), (b'hotel', b'Hotel'), (b'bed', b'Bed'), (b'viacoin', b'Viacoin'), (b'train', b'Train'), (b'subway', b'Subway'), (b'medium', b'Medium')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(null=True, verbose_name='admin note', blank=True)),
                ('title', models.CharField(help_text=b'The display title for this object.', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('slug', models.CharField(help_text=b'Auto-generated page slug for this object.', max_length=255, verbose_name='Slug', db_index=True, blank=True)),
                ('uuid', models.CharField(help_text=b'UUID generated for object; can be used for short URLs', max_length=255, verbose_name='UUID', blank=True)),
                ('order', models.IntegerField(default=0, help_text=b'')),
                ('path', models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='path', blank=True)),
                ('title_path', models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True)),
                ('path_generated', models.CharField(help_text=b'The URL path to this page, based on page hierarchy and slug.', max_length=255, null=True, verbose_name='generated path', blank=True)),
                ('path_override', models.CharField(help_text=b'The URL path to this page, defined absolutely.', max_length=255, null=True, verbose_name='path override', blank=True)),
                ('hierarchy', models.CharField(null=True, max_length=255, blank=True, help_text=b'Administrative Hierarchy', unique=True, verbose_name='hierarchy')),
                ('temporary_redirect', models.CharField(help_text=b'Temporarily redirect to a different path', max_length=255, verbose_name='Temporary Redirect', blank=True)),
                ('permanent_redirect', models.CharField(help_text=b'Permanently redirect to a different path', max_length=255, verbose_name='Permanent Redirect', blank=True)),
                ('publication_date', models.DateTimeField(null=True, verbose_name='Publication Date', blank=True)),
                ('publication_status', models.IntegerField(default=10, help_text=b'Current publication status', choices=[(10, 'Draft'), (20, 'Needs Review'), (100, 'Published'), (40, 'Unpublished')])),
                ('publish_on_date', models.DateTimeField(help_text=b"Object state will be set to 'Published' on this date.", null=True, verbose_name='Publish on Date', blank=True)),
                ('expire_on_date', models.DateTimeField(help_text=b"Object state will be set to 'Expired' on this date.", null=True, verbose_name='Expire on Date', blank=True)),
                ('page_meta_description', models.CharField(help_text=b'A short description of the page, used for SEO and not displayed to the user; aim for 150-160 characters.', max_length=2000, verbose_name='Meta Description', blank=True)),
                ('page_meta_keywords', models.CharField(help_text=b'A short list of keywords of the page, used for SEO and not displayed to the user; aim for 150-160 characters.', max_length=2000, verbose_name='Meta Page Keywords', blank=True)),
                ('is_searchable', models.BooleanField(default=True, help_text=b'Allow search engines to index this object and display in sitemap.')),
                ('in_sitemap', models.BooleanField(default=True, help_text=b'Is in sitemap')),
                ('noindex', models.BooleanField(default=False, help_text=b'Robots noindex')),
                ('nofollow', models.BooleanField(default=False, help_text=b'Robots nofollow')),
                ('sitemap_changefreq', models.CharField(default=b'monthly', help_text=b'How frequently does page content update', max_length=255, verbose_name='Sitemap Change Frequency', choices=[(b'never', 'Never'), (b'yearly', 'Yearly'), (b'monthly', 'Monthly'), (b'weekly', 'Weekly'), (b'daily', 'Daily'), (b'hourly', 'Hourly'), (b'always', 'Always')])),
                ('sitemap_priority', models.CharField(default=b'0.5', max_length=255, blank=True, help_text=b'Sitemap priority', null=True, verbose_name=b'Sitemap Priority')),
                ('shareable', models.BooleanField(default=False, help_text=b'Show sharing widget')),
                ('tiny_url', models.CharField(help_text=b'Tiny URL used for social sharing', max_length=255, null=True, verbose_name='tiny url', blank=True)),
                ('social_share_type', models.CharField(default=b'article', choices=[(b'article', b'Article'), (b'book', b'Book'), (b'profile', b'Profile'), (b'website', b'Website'), (b'video.movie', b'Video - Movie'), (b'video.episode', b'Video - Episode'), (b'video.tv_show', b'Video - TV Show'), (b'video.other', b'Video - Other'), (b'music.song', b'Music - Song'), (b'music.album', b'Music - Album'), (b'music.radio_station', b'Music - Playlist'), (b'music.radio_station', b'Music - Radio Station')], max_length=255, blank=True, null=True, verbose_name=b'Social type')),
                ('facebook_author_id', models.CharField(help_text=b'Numeric Facebook ID', max_length=255, null=True, verbose_name=b'Facebook Author ID', blank=True)),
                ('twitter_author_id', models.CharField(help_text=b'Twitter handle, including "@" e.g. @cgpartners', max_length=255, null=True, verbose_name=b'Twitter Admin ID', blank=True)),
                ('google_author_id', models.CharField(help_text=b'Google author id, e.g. the AUTHOR_ID in https://plus.google.com/AUTHOR_ID/posts', max_length=255, null=True, verbose_name=b'Google Admin ID', blank=True)),
                ('content', models.TextField(help_text=b'', null=True, verbose_name='content', blank=True)),
                ('synopsis', models.TextField(help_text=b'', null=True, verbose_name='synopsis', blank=True)),
                ('created_by', models.ForeignKey(related_name='account_usergroup_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserGroupMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(null=True, verbose_name='admin note', blank=True)),
                ('order', models.IntegerField(default=0, help_text=b'')),
                ('created_by', models.ForeignKey(related_name='account_usergroupmember_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('group', models.ForeignKey(blank=True, to='account.UserGroup', null=True)),
                ('modified_by', models.ForeignKey(related_name='account_usergroupmember_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
            },
        ),
    ]
