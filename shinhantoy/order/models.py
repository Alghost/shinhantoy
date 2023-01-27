from django.db import models

# Create your models here.

class Order(models.Model):
    ord_ymd = models.CharField(max_length=16, verbose_name='ORD_YMD')
    acct_mang_dbrn_code = models.CharField(max_length=16, verbose_name='ACCT_MANG_DBRN_CODE')
    ord_no = models.IntegerField(verbose_name='ORD_NO')
    acct_no = models.CharField(max_length=64, verbose_name='ACCT_NO')
    callv_type_code = models.CharField(max_length=32, verbose_name='CALLV_TYPE_CODE')
    sell_buy_tp_code = models.IntegerField(verbose_name='SELL_BUY_TP_CODE')
    stbd_code = models.CharField(max_length=16, verbose_name='STBD_CODE')
    ord_qty = models.IntegerField(verbose_name='ORD_QTY')
    ord_uv = models.IntegerField(verbose_name='ORD_UV')
    mrgn_base_uv = models.IntegerField(verbose_name='MRGN_BASE_UV')

    class Meta:
        db_table = 'shinhan_order'
        verbose_name = '주문정보'
        verbose_name_plural = '주문정보'

class Comment(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE, verbose_name='사용자')
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE, verbose_name='주문')
    content = models.TextField(verbose_name='내용')
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')

    class Meta:
        db_table = 'shinhan_order_comment'
        verbose_name = '주문정보 댓글'
        verbose_name_plural = '주문정보 댓글'