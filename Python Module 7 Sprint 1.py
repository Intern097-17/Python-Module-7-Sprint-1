#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import param
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pn.extension()

get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


df = pd.DataFrame({'Missing':['Activities', 'Reflections', 'Sprints'],
                  'Number':[10, 7, 1]}
)


# In[ ]:


class MissingNumbersDashboard(param.Parameterized):
    
    Missing = param.ObjectSelector(default='Activities', objects=list(df.Missing.unique()))
    
    
    def get_data(self):
        class_df = df[(df.Missing==self.Missing)].copy()
        return class_df
    
    
    def box_view(self):
        data = self.get_data()
        ax = snsboxplot(data('Number'))
        plt.close()
        return ax.figure
    
    def table_view(self):
        data = self.get_data()
        return data


# In[ ]:


dashboard_title = '# Missing Numbers Dashboard'

dashboard_desc = 'an example of a simple interactive HoloViz Panel dashboard using a set of data of missing Activities, Sprints and Reflections'


dashboard = pn.Column(dashboard_tile,
                     dashboard_desc,
                     rd.param,
                     rd.box_view,
                     rd.table_view
                     )


# In[ ]:




