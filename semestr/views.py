# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import  RequestContext
from django.shortcuts import render_to_response, render, redirect
from semestr import decoder
from semestr.filesystem import savetofile, savedict
from semestr.encoder import size_list_to_str
from semestr.forms import Signal_info
from math import log
from encoder import encode
from semestr.settings import STATIC_ROOT

def execute(request):
    if request.method == 'POST':
        form = Signal_info(request.POST)
        if form.is_valid():
            str = request.POST['signals']
            size_original = len(str)
            params = [int(s) for s in str.split()]
            step = int(request.POST['step'])
            params_by_step = params[::step]
            size_by_step = size_list_to_str(params_by_step)
            params_by_step_dict = to_dec(params_by_step)
            temp = encode(params_by_step, params_by_step_dict)
            encoded_params_by_step = temp[0]
            savetofile(encoded_params_by_step, 'encoded')
            binary_dict = temp[1]
            savedict(binary_dict, 'code_dict')
            size_encoded = len(encoded_params_by_step)
            return render_to_response('graphic_answer.html', {'params': params,
                                                              'entropy': round(entropy_unprepared(params), 2),
                                                              'params_by_step': params_by_step,
                                                              'entropy_step': round(entropy(params_by_step_dict, len(params_by_step)), 2),
                                                              'step': step,
                                                              'encoded_params_by_step':encoded_params_by_step,
                                                              'size_original':size_original,
                                                              'size_by_step':size_by_step,
                                                              'size_encoded':size_encoded,
                                                              'dict':binary_dict,
                                                              'or_en':size_original - size_encoded,
                                                              'or_step':size_original - size_by_step,
                                                              'step_en':size_by_step-size_encoded,
                                                              'decoded_signals':decoder.decode(encoded_params_by_step, binary_dict),
                                                              },
                context_instance=RequestContext(request))
    else:
        form = Signal_info()
    return render(request, 'preview.html', {'form': form})


def to_dec(signals):
    signal_dec = {}
    for signal in signals:
        signal_dec[signal] = signal_dec.get(signal, 0) + 1
    return signal_dec

def decode(request):
    if request.method == 'POST':
        code = request.POST['code']
        binary_dict = request.POST['dict']
        return render_to_response('decode.html', {'decoded_signals':decoder.decode(code, binary_dict),
                                                  'binary_dict':binary_dict,
                                                  'code':code
        },
            context_instance=RequestContext(request))

    else:
        return redirect('/decode')


def entropy(signal_dec, signal_count):
    sum = 0
    if signal_count != 0:
        for signal_key in signal_dec:
            p = float(signal_dec[signal_key]) / signal_count
            sum += 0 if p == 0 else p * ((log(p) / log(2)))
    return -sum

def entropy_unprepared(signals):
    sum = 0
    signal_dec = to_dec(signals)
    signal_count = len(signals)
    return entropy(signal_dec, signal_count)

def download_file(request):
  f = open(STATIC_ROOT + "/semestr.docx", 'rb')
  return HttpResponse(f, mimetype='application/octet-stream')

#def divide(signal_dec):
#    srt_dict = sorted(list(signal_dec.items()), key=lambda item: item[1],reverse=True)
#    spl_index = len(srt_dict) / 2
#    l_sum = sum([x[1] for x in srt_dict[: spl_index]])
#    r_sum = sum([x[1] for x in srt_dict[spl_index:]])
#    print "yes"
#    while True:
#        delta = l_sum - r_sum
#        if (delta > 0):
#            spl_index_temp = spl_index - 1
#        else:
#            spl_index_temp = spl_index
#        l_sum = l_sum  - srt_dict[spl_index_temp][1]
#        r_sum = r_sum + srt_dict[spl_index_temp][1]
#        if (abs(delta) >= abs(l_sum - r_sum)):
#            spl_index = spl_index_temp
#        else:
#            return ([x for x in srt_dict[:spl_index]],[x for x in srt_dict[spl_index:]])
