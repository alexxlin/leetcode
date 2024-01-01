func addBinary(a string, b string) string {
    i, j := len(a)-1, len(b)-1
    carry := 0
    ret := []string{}

    for i >= 0 && j >= 0 {
        tmp := int(a[i]- '0')+int(b[j]-'0')+carry
        tret := tmp % 2 
        carry = tmp / 2
        ret = append([]string{fmt.Sprintf("%d", tret)}, ret...)
        i--
        j--
    }
    for i >= 0 {
        tmp := int(a[i]- '0')+carry
        tret := tmp % 2 
        carry = tmp / 2
        ret = append([]string{fmt.Sprintf("%d", tret)}, ret...)
        i--
    }

    for j >= 0 {
        tmp := int(b[j]- '0')+carry
        tret := tmp % 2 
        carry = tmp / 2
        ret = append([]string{fmt.Sprintf("%d", tret)}, ret...)
        j--
    }
    if carry == 1 {
        ret = append([]string{"1"}, ret...)
    }
    return strings.Join(ret, "")
}

