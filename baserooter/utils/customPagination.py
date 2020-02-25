from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from math import ceil
import operator
from functools import reduce
from django.db.models import Q
from datetime import datetime


class CustomPagination:

    def get_custom_pagination(request, model, search_keys, search_type, serializer, query):
        """ Function to handle custom pagination"""
        length = request.data['length']
        start = request.data['start']
        columns_order = request.data['order'][0]['column']
        order = request.data['columns'][columns_order]['data']
        direction = request.data['order'][0]['dir']
        search_value = request.data['search']['value']
        try:
            from_date = request.data['search']['from_date']
            to_date = request.data['search']['to_date']
        except:
            from_date = None
            to_date = None

        if (direction == 'desc'):
            order = '-' + order

        if (direction == 'undefined'):
            order = '-id'


        if (from_date =='' or from_date ==None) and (to_date =='' or to_date ==None):
            from_date = None
            to_date = None

        elif (from_date !='' or from_date !=None) and (to_date =='' or to_date ==None):
            start_date = str(from_date).split('-')
            from_date = datetime(int(start_date[0]), int(start_date[1]), int(start_date[2]))
            today = datetime.now()
            to_date = today
        else:
            start_date = str(from_date).split('-')
            from_date = datetime(int(start_date[0]), int(start_date[1]), int(start_date[2]))
            end_date = str(to_date).split('-')
            to_date = datetime(int(end_date[0]), int(end_date[1]), int(end_date[2])+1)            
            

        kwargs = []
        if (search_value):
            no_of_keys = len(search_keys)
            if no_of_keys > 0:
                for keyname in search_keys:
                    kwargs.append(Q(**{keyname:search_value}))

                if(search_type == 'and'):
                    if from_date == None and to_date == None:                   
                        query = query.filter(reduce(operator.and_, kwargs))
                    else:                   
                        query = query.filter(reduce(operator.and_, kwargs),created_at__range=[from_date,to_date])
                else:
                    
                    if from_date == None and to_date == None:                   
                        query = query.filter(reduce(operator.or_, kwargs))
                    else:                   
                        query = query.filter(reduce(operator.or_, kwargs),created_at__range=[from_date,to_date])

        else:
            if (from_date == None )and (to_date == None):
                query = model.objects.all()
                
            else:                
                query = model.objects.filter(created_at__range=[from_date,to_date])


        page_no = int(start/length + 1)
        query = query.order_by(order)
        print(len(query),length)
        paginator = Paginator(query, length)
        paginated_data = paginator.page(page_no)
        serializer = serializer(paginated_data, many=True)
        return {"response_data": serializer.data, "total_records": paginated_data.paginator.count}

