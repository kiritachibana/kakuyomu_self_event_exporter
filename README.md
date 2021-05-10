# kakuyomu_self_event_exporter

## Overview

This is a tool to scrap Kakuyomu's self event page and export to TSV (Tab separated file).

* Required: Python 3+, BeautifulSoup

## Configuration

1. Open self_event_exporter.py and edit "target_url" as you want to export.
2. Then save it and run the script like as below:
   ```
   $ python self_event_exporter.py
   ```

Then you will see the result like as below:

```
Title	Author	URL	Genre	Status	Episodes	Characters Rating
海の王と風の娘	橘 紀里	https://kakuyomu.jp/works/1177354054917676869	恋愛	完結済	45	200159 108
```
