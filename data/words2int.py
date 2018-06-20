# -*- coding: utf-8 -*-

import os


# data example in each file
# avid:1 your:1 horrible_book:1 wasted:1 use_it:1 the_entire:1 money.i:1 i_lit:1 i_read:1 lit:1 i_would:1 relationship:1 read:1 a_<num>:1 reader_and:1 reader:1 suffering:1 fire_one:1 i_had:1 year_old:2 gotten:1 horrible:3 lit_this:1 world...don't:1 my:2 one_star:1 headache_the:1 this_book:5 mom:1 was_horrible:1 friend:1 book_horrible:1 star_i:1 back:1 avid_reader:1 than_one:1 life:1 copy:1 rate_it:1 rate:1 my_mom:1 man:1 book_was:1 half:1 on_fire:1 and_then:1 reading_this:1 so:1 lower:1 i_could:1 <num>_year:2 than:1 time:2 half_of:1 time_spent:1 then:1 book:6 and_picked:1 possible:1 spent:1 old_man:1 up_after:1 one:2 horrible_if:1 one_less:1 part:1 was:2 entire:1 less_copy:1 to_rate:1 my_life:1 about_the:1 your_money.i:1 an_avid:1 if:1 the_relationship:1 use:1 a_headache:1 fire:1 lower_than:1 reading:1 a_friend:1 picked:1 purposes:1 then_got:1 waste_your:1 after_my:1 friend_i:1 old:2 man_and:1 and_i:1 world...don't_waste:1 book_on:1 part_about:1 copy_in:1 book_back:1 book_wasted:1 have_i:1 time_and:1 the_world...don't:1 better:1 if_it:1 star:1 got:1 mom_had:1 read_half:1 waste:1 after:1 i:6 about:1 could_use:1 had_gotten:1 was_possible:1 year:2 it_lower:1 relationship_the:1 wasted_my:1 wish:1 wish_i:1 boy:1 purposes_this:1 got_to:1 the_time:1 it_was:1 back_so:1 suffering_from:1 spent_reading:1 book_up:1 less:1 better_purposes:1 headache:1 possible_to:1 money.i_wish:1 for_better:1 it_suffering:1 the_part:1 gotten_it:1 picked_this:1 entire_time:1 old_boy:1 i_am:1 the_<num>:1 boy_had:1 <num>:2 so_i:1 #label#:negative

def idem_mkdir(dir_path):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)


def gen_dir_file(dir_path):
    for d in sorted(os.listdir(source_dir)):
        if '.DS' in d: continue
        for f in sorted(os.listdir(source_dir + '/' + d)):
            if '.DS' in d: continue
            yield d, f


def init_dir(source_dir, target_dir):
    idem_mkdir(target_dir)
    for d, _ in gen_dir_file(source_dir):
        idem_mkdir(target_dir + '/' + d)


def get_as_dict(line):
    d = dict()
    for item in line.strip().split(' ')[:-1]:
        term, value = item.split(':')
        d[term] = value
    return d


source_dir = 'processed_acl'
target_dir = 'data'

init_dir(source_dir, target_dir)
w2i = dict()
for d, f in gen_dir_file(source_dir):
    print('processing...', d, f)
    converted_datum = list()
    for l in open('/'.join([source_dir, d, f])):
        converted_data = list()
        for k, v in get_as_dict(l).items():
            if k not in w2i: w2i[k] = str(len(w2i))
            converted_data.append(w2i[k] + ':' + v)
        converted_datum.append(' '.join(converted_data))
    with open('/'.join([target_dir, d, f]), 'w') as fp:
        fp.write('\n'.join(converted_datum))
