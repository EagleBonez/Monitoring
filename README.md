# Monitoring

Summary:
Database for monitoring the progress of housing sites with planning approval e.g. planning applications which have been granted planning permission, sites where Planning Committee has resolved to grant planning permission, and sites allocated in a Local Plan or Neighourhood Plan.

Planning approvals have many different attributes and statuses e.g. a planning application may be 'extant' (live), 'complete' (all dwellings built out), 'superseded' (replaced by another application), or lapsed (not implemented before expiry date). Planning permissions may be 'outline', 'full', 'reserved matters', etc.

Monitoring data needs to be accurate down to the level of individual plots e.g. "Plot 1, 3-bed, affordable tenure, house, commenced development 01 May 2020".

Councils have a legal requirement to monitor this data and return the data to government in various different formats and for different purposes. The data has many different applications in day-to-day council business.

Councils are required to, each year, produce a 'housing trajectory' which projects future delivery rates of housing over the next 10-20 years or so, and must publish a 'Five Year Housing Land Supply Report'. 

Whether a Council can demonstrate it has five year's worth of housing land is a really important issue. At planning appeals developers will try to 'prove' a council doesn't have sufficient sites (i.e. undermine the five year housing land supply data). The Council then has the task of defending its data.

Objectives:
- Accurately monitor housing to the level of individual plots i.e. ensure there is no double counting of superseded or phased apps, return data correct at specific points in time, enable council to fulfil all its legal duties for returning data to govt,  preparing Annual Monitoring Report, housing trajectory and Five Year Housing Land Supply Report, etc.

- Make data transparent and accessible. Use permissions to control who can see what. Within the Council, some people require editing rights, others to view data only. The data could also be made viewable and downloadable for the public - no other system does this, and it would be a major benefit in providing transparency and accessibility. At appeals it would benefit both the council and developers. If the data is presented clearly, it'd make it less likely to misinterpret/undermine the data (strengthening Council's case), for developers it'll make their lives easier as data clearer and more accessible.

- Perform calculations on data to show stats at various points in time. e.g. current net commitment, dwellings completed on site to date, etc. Could even calculate Five Year Housing Land Supply, Local Housing Need, etc.

- It is highly desirable to include web cartography to display the locations of sites with planning permission. I've done a few projects showing geoJSON data using Leaflet JS library on Open Street Map map base. Perhaps better investigating geodjango. But should be acheivable.

Structure of database:
The database structure is relatively simple:

- 'Sites' is simply a way of grouping planning apps which relate to the same area of land. i.e. one site can relate to many planning apps

- 'Planning Approvals'- attributes relating to planning app, such as development type, number of units, etc. (there are a lot of fields!).

- 'Plots' - each planning app may have many plots e.g. a planning app with a site capacity of 10 has 10 plots. A planning app could have 1 plot or several thousand! Also a plot can be a negative, i.e. a net loss through demolition.

- 'Notes' - enables users to add multiple file notes to the planning app. The one to many relationship means a new note can be created without needing to delete older notes, thereby providing an audit trail.

- There is also a 'Parish' model to identify the civil parish in which planning app is located. I am trying to figure out how to create a 'nested query' to show settlements in the selected parish. 


Summary of work to date:
I have:
- Created all models with all required fields. However I still need to add a few @property attributes to calculate current status of planning app accurately, and still need to add help text and verbose names for some fields.

- Customised admin page to make it reasonably user friendly.

- Created urls and views for adding/editing models, for logging in registered users, for showing detail and listing sites/planning apps, etc.

- Created templates for all/most views and added bootstrap containers and styling. If the styling looks a bit off its probably because the pi is set up for a 4k screen!

- Added a date picker and begun customising some widgets. Made tables sortable.

- Wherever possible I have tried to use generic and built in django methods to avoid running into probs.


Outstanding issues:
- I am having difficulties with 'planning_app_form' template. This is the main form in the database used for adding/editing planning apps, and related plots and notes via formsets. I am running into validation errors when I try to do clever stuff with the formsets. I need to be able to dynamically add formset instances (especially for plots), and present the formset data in a clear way.

- Also in same form, trajectory fields not showing in table

- Need to add remaining @property attributes for calcs

- Add nested query for settlement, based on parish choice

- Create a choice field for superseded apps

- All form and view templates still need tidying up, javascript functions for search, etc. 

- Need to figure out how to show trajectory table data in view better

- Need to create functions for importing/exporting csv data.e.g. import relevant apps which require montoring in database; export trajectory data, etc.

- Web mapping stuff.

- Configure view/edit permissions.
