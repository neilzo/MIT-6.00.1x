# Counting and Grouping
# Passes with 'order = "salad water hamburger salad hamburger" returns "salad:2 hamburger:2 water:1"'
# Or 'order = "hamburger water hamburger" returns "salad:0 hamburger:2 water:1"'
order = "salad water hamburger salad hamburger"
order_1 = "hamburger water hamburger"

test_cond = "salad:2 hamburger:2 water:1"
test_cond_1 = "salad:0 hamburger:2 water:1"


def item_order(order):
    salad_ctn = 0
    hamburger_ctn = 0
    water_ctn = 0

    concat_order = order.replace(' ', '')

    salad_ctn = concat_order.count('salad')
    hamburger_ctn = concat_order.count('hamburger')
    water_ctn = concat_order.count('water')

    return 'salad:%d hamburger:%d water:%d' % (salad_ctn, hamburger_ctn, water_ctn)

print item_order(order) == test_cond
print item_order(order_1) == test_cond_1
