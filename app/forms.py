from django.forms import ModelForm
from app.models import Valores

class ValoresForm(ModelForm):
  class Meta:
    model = Valores
    fields = [
      'entrada', 
      'data', 
      'produto', 
      'h_disp', 
      'q_cs', 
      'ag_tq_fus', 
      'bat_tq_fus',
      'bb_fus',
      'q_sol',
      'hh_prog',
      'ag_tq_car', 
      'bat_tq_mis', 
      'bb_mis' ,
      'ag_tq_ali', 
      'bb_ali', 
      'acc_maq_form', 
      'acc_trans_estoc', 
      'q_mf_real', 
      'aprov_qual' 
    ]