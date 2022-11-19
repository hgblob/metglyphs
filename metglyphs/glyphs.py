"""Glyph set names and lookup tables for glyph file names."""

# Constants for available set names
YRNO_GLYPHS = 'yrno'
MET_OFFICE_GLYPHS = 'metoffice'
WEATHER_ICONS_IO_GLYPHS = 'weathericonsio'
DEFAULT_GLYPHS = MET_OFFICE_GLYPHS


# Lookup tables for wmo code to filename for each glyph set
# Paths are relative to assets/<set_name>/
WMO_GLYPH_LOOKUP = {
    YRNO_GLYPHS: {
        "00d": "01d.1.svg",
        "00n": "01n.1.svg",
        '01d': '02d.1.svg',
        '01n': '02n.1.svg',
        '03d': '04.1.svg',
        '10d': '15.1.svg',
        '14d': '15.1.svg',
        '30d': '15.1.svg',
        '50d': '46.1.svg',
        '60d': '09.1.svg',
        '63d': '10.1.svg',
        '65d': '12.1.svg',
        '65n': '12.1.svg',
        '70d': '13.1.svg',
        '75d': '48.1.svg',
        '81d': '05d.1.svg',
        '81n': '05n.1.svg',
        '83d': '41d.1.svg',
        '83n': '41n.1.svg',
        '85d': '08d.1.svg',
        '85n': '08n.1.svg',
        '87d': '45d.1.svg',
        '87n': '45n.1.svg',
        '89d': '43d.1.svg',
        '89n': '43n.1.svg',
        '90d': '30.1.svg',
        '95d': '25d.1.svg',
        '95n': '25n.1.svg'
    },
    MET_OFFICE_GLYPHS: {
        "00d": "1.svg",
        "00n": "0.svg",
        '01d': '3.svg',
        '01n': '2.svg',
        '03d': '7.svg',
        '10d': '5.svg',
        '14d': '8.svg',
        '30d': '5.svg',
        '50d': '11.svg',
        '60d': '10.svg',
        '63d': '15.svg',
        '65d': '17.svg',
        '65n': '16.svg',
        '70d': '23.svg',
        '75d': '21.svg',
        '81d': '10.svg',
        '81n': '9.svg',
        '83d': '14.svg',
        '83n': '13.svg',
        '85d': '23.svg',
        '85n': '22.svg',
        '87d': '26.svg',
        '87n': '25.svg',
        '89d': '20.svg',
        '89n': '19.svg',
        '90d': '30.svg',
        '95d': '29.svg',
        '95n': '28.svg'
    },
    WEATHER_ICONS_IO_GLYPHS: {
            "00d": "wi-day-sunny.svg"
            "00n": "wi-night-clear.svg",
            '01d': 'wi-day-cloudy.svg',
            '01n': 'wi-night-cloudy.svg',
            '02d': 'wi-thermometer.svg',
            '03d': 'wi-cloud.svg',
            '04d': 'wi-fog.svg',
            '05d': 'wi-fog.svg',
            '10d': 'wi-day-fog.svg',
            '11d': 'wi-fog.svg',
            '12d': 'wi-lightning.svg',
            '14d': 'wi-cloudy.svg',
            '18d': 'wi-strong-wind.svg',
            '20d': 'wi-fog.svg',
            '21d': 'wi-rain-mix.svg',
            '22d': 'wi-rain-mix.svg',
            '23d': 'wi-rain.svg',
            '24d': 'wi-snow.svg',
            '25d': 'wi-hail.svg',
            '26d': 'wi-thunderstorm.svg',
            '27d': 'wi-dust.svg',
            '28d': 'wi-dust.svg',
            '29d': 'wi-dust.svg',
            '30d': 'wi-fog.svg',
            '31d': 'wi-fog.svg',
            '32d': 'wi-fog.svg',
            '33d': 'wi-fog.svg',
            '34d': 'wi-fog.svg',
            '35d': 'wi-fog.svg',
            '40d': 'wi-rain-mix.svg',
            '41d': 'wi-sprinkle.svg',
            '42d': 'wi-rain.svg',
            '43d': 'wi-sprinkle.svg',
            '44d': 'wi-rain.svg',
            '45d': 'wi-hail.svg',
            '46d': 'wi-hail.svg',
            '47d': 'wi-snow.svg',
            '48d': 'wi-snow.svg',
            '50d': 'wi-sprinkle.svg',
            '51d': 'wi-sprinkle.svg',
            '52d': 'wi-rain.svg',
            '53d': 'wi-rain.svg',
            '54d': 'wi-snowflake-cold.svg',
            '55d': 'wi-snowflake-cold.svg',
            '56d': 'wi-snowflake-cold.svg',
            '57d': 'wi-sprinkle.svg',
            '58d': 'wi-rain.svg',
            '60d': 'wi-rain.svg',
            '61d': 'wi-sprinkle.svg',
            '62d': 'wi-rain.svg',
            '63d': 'wi-rain-wind.svg',
            '64d': 'wi-hail.svg',
            '65d': 'wi-day-rain-mix.svg',
            '65n': 'wi-night-alt-rain-mix.svg',
            '66d': 'wi-hail.svg',
            '67d': 'wi-rain-mix.svg',
            '68d': 'wi-rain-mix.svg',
            '70d': 'wi-snow.svg',
            '71d': 'wi-snow.svg',
            '72d': 'wi-snow.svg',
            '73d': 'wi-snow.svg',
            '74d': 'wi-snowflake-cold.svg',
            '75d': 'wi-snowflake-cold.svg',
            '76d': 'wi-snowflake-cold.svg',
            '77d': 'wi-snow.svg',
            '78d': 'wi-snowflake-cold.svg',
            '80d': 'wi-rain.svg',
            '81d': 'wi-day-showers.svg',
            '81n': 'wi-night-alt-showers.svg',
            '82d': 'wi-rain.svg',
            '83d': 'wi-day-rain.svg',
            '83n': 'wi-night-rain.svg',
            '84d': 'wi-storm-showers.svg',
            '85d': 'wi-day-snow.svg',
            '85n': 'wi-night-alt-snow.svg',
            '86d': 'wi-rain-mix.svg',
            '87d': 'wi-day-snow-wind.svg',
            '87n': 'wi-night-alt-snow-wind.svg',
            '89d': 'wi-day-hail.svg',
            '89n': 'wi-night-alt-hail.svg',
            '90d': 'wi-lightning.svg',
            '91d': 'wi-storm-showers.svg',
            '92d': 'wi-thunderstorm.svg',
            '93d': 'wi-thunderstorm.svg',
            '94d': 'wi-lightning.svg',
            '95d': 'wi-day-thunderstorm.svg',
            '95n': 'wi-night-alt-thunderstorm.svg'
            '96d': 'wi-thunderstorm.svg',
            '99d': 'wi-tornado.svg'
    }
}
