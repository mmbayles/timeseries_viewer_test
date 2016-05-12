from tethys_sdk.base import TethysAppBase, url_map_maker


class TimeSeriesViewerTest(TethysAppBase):
    """
    Tethys app class for Time Series Viewer Test.
    """

    name = 'Time Series Viewer Test'
    index = 'timeseries_viewer_test:home'
    icon = 'timeseries_viewer_test/images/icon.gif'
    package = 'timeseries_viewer_test'
    root_url = 'timeseries-viewer-test'
    color = '#f1c40f'
    description = 'Place a brief description of your app here.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='timeseries-viewer-test',
                           controller='timeseries_viewer_test.controllers.home'),
                    # UrlMap(name='temp_waterml',
                    #        url='temp_waterml/{id}',
                    #        controller='timeseries_viewer_test.controllers.temp_waterml'),

                    UrlMap(name='chart_data',
                           url='chart_data/{res_id}/{src}',
                           controller='timeseries_viewer_test.controllers.chart_data'),

                    UrlMap(name='api',
                           url='api',
                           controller='timeseries_viewer_test.api.home'),

                    UrlMap(name='api_list_apps',
                           url='api/list_apps',
                           controller='timeseries_viewer_test.api.list_apps'),

                    UrlMap(name='api_list_apps_help',
                           url='api/list_apps_help',
                           controller='timeseries_viewer_test.api.list_apps_help')
        )

        return url_maps