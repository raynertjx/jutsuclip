"use client";

import { zodResolver } from "@hookform/resolvers/zod";
import { useFieldArray, useForm } from "react-hook-form";
import * as z from "zod";
import { Button } from "@/components/ui/button";
import { Form, FormControl, FormField, FormItem } from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { Textarea } from "../ui/textarea";

const formSchema = z.object({
  inputs: z.array(
    z.object({
      value: z.optional(z.string().max(200)),
    })
  ),
});

export function FieldForm() {
  type FormValues = z.infer<typeof formSchema>;
  const storedInputs = localStorage.getItem("inputs");
  // console.log(JSON.parse(storedInputs));
  if (storedInputs) console.log(JSON.parse(storedInputs).inputs[0].value);

  const defaultValues: Partial<FormValues> = {
    inputs: [
      { value: storedInputs ? JSON.parse(storedInputs).inputs[0].value : "" },
      { value: storedInputs ? JSON.parse(storedInputs).inputs[1].value : "" },
      { value: storedInputs ? JSON.parse(storedInputs).inputs[2].value : "" },
      { value: storedInputs ? JSON.parse(storedInputs).inputs[3].value : "" },
      { value: storedInputs ? JSON.parse(storedInputs).inputs[4].value : "" },
      { value: storedInputs ? JSON.parse(storedInputs).inputs[5].value : "" },
    ],
  };

  // 1. Define your form.
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues,
  });

  const { fields } = useFieldArray({
    name: "inputs",
    control: form.control,
  });

  // 2. Define a submit handler.
  function onSubmit(values: z.infer<typeof formSchema>) {
    // Do something with the form values.
    // ✅ This will be type-safe and validated.
    console.log(values);
    localStorage.setItem("inputs", JSON.stringify(values));
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
        {fields.map((field, index) => (
          <FormField
            control={form.control}
            key={field.id}
            name={`inputs.${index}.value`}
            render={({ field }) => (
              <FormItem>
                <FormControl>
                  <Textarea {...field} />
                </FormControl>
              </FormItem>
            )}
          />
        ))}
        <Button type="submit">Submit</Button>
      </form>
    </Form>
  );
}
