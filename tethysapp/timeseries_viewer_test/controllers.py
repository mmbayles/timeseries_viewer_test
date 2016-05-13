from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from wsgiref.util import FileWrapper
import os
import csv
import json
from datetime import datetime
import utilities
import tempfile
import pandas

# -- coding: utf-8--

# helper controller for fetching the WaterML file
# def temp_waterml(request, id):
#     base_path = utilities.get_workspace()+"/id"
#     file_path = base_path + "/" +id
#     response = HttpResponse(FileWrapper(open(file_path)), content_type='application/xml')
#
#     return response


# formats the time series for highcharts
def chart_data(request, res_id, src):
    print "start chart_data"
    print datetime.now()
    # checks if we already have an unzipped xml file
    file_path = utilities.waterml_file_path(res_id)
    # if we don't have the xml file, downloads and unzips it
    if not os.path.exists(file_path):
        utilities.unzip_waterml(request, res_id,src)

    # returns an error message if the unzip_waterml failed
    if not os.path.exists(file_path):
        data_for_chart = {'status': 'Resource file not found'}
    else:
        # parses the WaterML to a chart data object
        data_for_chart = utilities.Original_Checker(file_path,res_id)
        # print data_for_chart

        # print datetime.now()
    # csv_file = utilities.get_workspace() + "/id/master.csv"

    # print csv_file
    print "JSON Reponse"
    print datetime.now()
    # data = []
    # data1 = []
    # with open(csv_file) as csvfile:
    #     reader = csv.reader(csvfile, delimiter = ',', quotechar = "'")
    #     # data1 = map(float,reader)
    #
    #     counter = 0
    #     for row in reader:
    #
    #         if counter ==0:
    #             print "first line"
    #         else:
    #             data.append(row)
    #         # print row
    #         counter = counter +1
    #
    # chart ={"for_highchart":data}
    # chart =  json.dumps(data_for_chart, sort_keys =True)
    # response = HttpResponse(chart, content_type="text/plain")
    return JsonResponse(data_for_chart )
    # return response
# home page controller
def home(request):


    context = {}
    return render(request, 'timeseries_viewer_test/home.html', context)

