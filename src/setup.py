from setuptools import setup
import setup_translate

pkg = 'Extensions.StreamTV'
setup(name='enigma2-plugin-extensions-streamtv',
       version='3.0',
       description='iptv player',
       package_dir={pkg: 'StreamTV'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'icons/*.png']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
