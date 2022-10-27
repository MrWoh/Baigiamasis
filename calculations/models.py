from django.db import models
from django.contrib.auth import get_user_model
from datetime import date


# class Calculations(models.Model):
#     calc_name = models.CharField('', max_length=50,
#                                  help_text='Pavadinimas')
#     unit_1 = models.DecimalField('', max_digits=6, decimal_places=2,
#                                  help_text='Svoris')
#     price_1 = models.DecimalField('', max_digits=6, decimal_places=2,
#                                   help_text='Kaina')
#     price_output_1 = models.DecimalField('', max_digits=6, decimal_places=2,
#                                          help_text='Išeiga')
#     unit_2 = models.DecimalField('', max_digits=6, decimal_places=2,
#                                  help_text='Svoris')
#     price_2 = models.DecimalField('', max_digits=6, decimal_places=2,
#                                   help_text='Kaina')
#     price_output_2 = models.DecimalField('', max_digits=6, decimal_places=2,
#                                          help_text='Išeiga')
#     unit_3 = models.DecimalField('', max_digits=6, decimal_places=2,
#                                  help_text='Svoris')
#     price_3 = models.DecimalField('', max_digits=6, decimal_places=2,
#                                   help_text='Kaina')
#     price_output_3 = models.DecimalField('', max_digits=6, decimal_places=2,
#                                          help_text='Išeiga')
#     unit_4 = models.DecimalField('', max_digits=6, decimal_places=2,
#                                  help_text='Svoris')
#     price_4 = models.DecimalField('', max_digits=6, decimal_places=2,
#                                   help_text='Kaina')
#     price_output_4 = models.DecimalField('', max_digits=6, decimal_places=2,
#                                          help_text='Išeiga')
#     unit_5 = models.DecimalField('', max_digits=6, decimal_places=2,
#                                  help_text='Svoris')
#     price_5 = models.DecimalField('', max_digits=6, decimal_places=2,
#                                   help_text='Kaina')
#     price_output_5 = models.DecimalField('', max_digits=6, decimal_places=2,
#                                          help_text='Išeiga')
#     no_vat_price = models.DecimalField('', max_digits=6, decimal_places=2,
#                                        help_text='Kaina Be PVM')
#     vat_price = models.DecimalField('', max_digits=6, decimal_places=2,
#                                     help_text='Kaina Su PVM')
#     sell_price = models.DecimalField('', max_digits=6, decimal_places=2,
#                                      help_text='Pardavimo Kaina')
#     cost_procentage = models.DecimalField('', max_digits=6, decimal_places=2,
#                                           help_text='savikaina')

#     calc_creator = models.ForeignKey(
#         get_user_model(),
#         verbose_name=("owner"),
#         on_delete=models.SET_NULL,
#         null=True, blank=True,
#     )
#     date_created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return '{} {} {}'.format(str(self.calc_name), str(self.calc_creator), str(self.date_created))
