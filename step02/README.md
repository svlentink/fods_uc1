# Step02 pandas

Quick debugging:
```shell
docker run -it --rm \
  -v /tmp/dataset:/datadir \
  --entrypoint python3 \
  continuumio/anaconda3
```

## Links
+ http://api.mongodb.com/python/current/tutorial.html
+ https://canvas.uva.nl/courses/2046/discussion_topics/18603


## Data layout
Not all rows have all fields!

### interesting
```
  "lang": "en",
  "timestamp_ms": "1470996289806"
  "place": {
    "country_code": "AU",
  "user": {
    "followers_count": 3482,
  "text": "@Geraldanthro @NeilTurner_ @realDonaldTrump want to do a comparison try maimed Vets pre &amp; post Iraq pullout. Bar graph that. @washingtonpost",

```

### Example
This is the very first row:
```json
{
  "created_at": "Fri Aug 12 10:04:49 +0000 2016",
  "id": 7.6403993277606e+17,
  "id_str": "764039932776058881",
  "text": "@Geraldanthro @NeilTurner_ @realDonaldTrump want to do a comparison try maimed Vets pre &amp; post Iraq pullout. Bar graph that. @washingtonpost",
  "source": "<a href=\"http:\/\/twitter.com\" rel=\"nofollow\">Twitter Web Client<\/a>",
  "truncated": false,
  "in_reply_to_status_id": 7.6403722350333e+17,
  "in_reply_to_status_id_str": "764037223503331328",
  "in_reply_to_user_id": 11966392,
  "in_reply_to_user_id_str": "11966392",
  "in_reply_to_screen_name": "Geraldanthro",
  "user": {
    "id": 740623508,
    "id_str": "740623508",
    "name": "michael halliday777",
    "screen_name": "michaelhallida4",
    "location": "Queensland OZ",
    "url": null,
    "description": "CE27HE27OE27NE26PE25SE24CaE25KE24ClE24NaE24MgE24FeE23FE23\nZnE22SiE22CuE21BE21IE20SnE20MnE20SeE20CrE20NiE20MoE19CoE19VE18 Human being,being human,last days !",
    "protected": false,
    "verified": false,
    "followers_count": 3482,
    "friends_count": 3382,
    "listed_count": 98,
    "favourites_count": 35521,
    "statuses_count": 84536,
    "created_at": "Mon Aug 06 13:27:59 +0000 2012",
    "utc_offset": -25200,
    "time_zone": "Pacific Time (US & Canada)",
    "geo_enabled": true,
    "lang": "en",
    "contributors_enabled": false,
    "is_translator": false,
    "profile_background_color": "C0DEED",
    "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_tile": false,
    "profile_link_color": "0084B4",
    "profile_sidebar_border_color": "C0DEED",
    "profile_sidebar_fill_color": "DDEEF6",
    "profile_text_color": "333333",
    "profile_use_background_image": true,
    "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/3688925705\/aced4cffb52675eda9a601284f64f60e_normal.jpeg",
    "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/3688925705\/aced4cffb52675eda9a601284f64f60e_normal.jpeg",
    "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/740623508\/1369117283",
    "default_profile": true,
    "default_profile_image": false,
    "following": null,
    "follow_request_sent": null,
    "notifications": null
  },
  "geo": null,
  "coordinates": null,
  "place": {
    "id": "004ec16c62325149",
    "url": "https:\/\/api.twitter.com\/1.1\/geo\/id\/004ec16c6232514sbane, Queensland",
    "country_code": "AU",
    "country": "Australia",
    "bounding_box": {
      "type": "Polygon",
      "coordinates": [
        [
          [
            152.668523,
            -27.767441
          ],
          [
            152.668523,
            -26.996845
          ],
          [
            153.31787,
            -26.996845
          ],
          [
            153.31787,
            -27.767441
          ]
        ]
      ]
    },
    "attributes": {
      
    }
  },
  "contributors": null,
  "is_quote_status": false,
  "retweet_count": 0,
  "favorite_count": 0,
  "entities": {
    "hashtags": [
      
    ],
    "urls": [
      
    ],
    "user_mentions": [
      {
        "screen_name": "Geraldanthro",
        "name": "Anthropologist",
        "id": 11966392,
        "id_str": "11966392",
        "indices": [
          0,
          13
        ]
      },
      {
        "screen_name": "NeilTurner_",
        "name": "Neil Turner",
        "id": 3600539122,
        "id_str": "3600539122",
        "indices": [
          14,
          26
        ]
      },
      {
        "screen_name": "realDonaldTrump",
        "name": "Donald J. Trump",
        "id": 25073877,
        "id_str": "25073877",
        "indices": [
          27,
          43
        ]
      },
      {
        "screen_name": "washingtonpost",
        "name": "Washington Post",
        "id": 2467791,
        "id_str": "2467791",
        "indices": [
          129,
          144
        ]
      }
    ],
    "symbols": [
      
    ]
  },
  "favorited": false,
  "retweeted": false,
  "filter_level": "low",
  "lang": "en",
  "timestamp_ms": "1470996289806"
}
```
