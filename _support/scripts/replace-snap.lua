function Span(elem)
  if elem.classes:includes('snap') and #elem.content == 1 then
    local str = elem.content[1]
    if str.t == 'Str' and str.text == 'Snap' then
      return pandoc.RawInline('latex', 'Snap\\texttt{!}')
    end
  end
end
