def make_draft(types,spec,actual,judgment,remark,count):
    title=' / '.join(types) if types else '검사'
    result=''
    action=''
    if spec or actual or remark:
        bits=[]
        if actual: bits.append(f'확인 결과 {actual}')
        if spec: bits.append(f'적용 기준 {spec}')
        if remark: bits.append(f'특이사항 {remark}')
        result=f"{title} 결과, " + ', '.join(bits) + f". 최종 판정은 {judgment}임."
        action={'합격':'별도 조치사항 없음.','불합격':'부적합 부위를 수정·보수한 후 동일 기준으로 재검사하고 결과를 확인할 것.','조건부 합격':'지정된 보완사항을 완료하고 객관적 증빙을 확인한 후 최종 승인할 것.','N/A':'해당 없음.'}[judgment]
    caption=f"사진 1~{count}: {title} 대상 및 확인 상태" if count else ''
    return result,action,caption
